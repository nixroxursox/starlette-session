import sys
import time
from datetime import datetime
from uuid import uuid4

from starlette.datastructures import Headers
from starlette.types import ASGIApp, Scope, Send, Receive, Message
from starlette.responses import Response
from starlette.requests import Request

from webob.cookies import JSONSerializer
#from flask.sessions import SessionInterface as FlaskSessionInterface
#from flask.sessions import SessionMixin
from werkzeug.datastructures import CallbackDict
from itsdangerous import Signer, BadSignature, want_bytes

from db.database import dataBase
from decouple import config 

PY2 = sys.version_info[0] == 2
if not PY2:
    text_type = str
else:
    text_type = unicode


def total_seconds(td):
    return td.days * 60 * 60 * 24 + td.seconds


class ServerSideSession(CallbackDict):
    """Baseclass for server-side based sessions."""

    def __init__(self, initial=None, sid=None, permanent=None):
        def on_update(self):
            self.modified = True
        CallbackDict.__init__(self, initial, on_update)
        self.sid = sid
        if permanent:
            self.permanent = permanent
        self.modified = False


class RedisSession(ServerSideSession):
    pass


class MemcachedSession(ServerSideSession):
    pass


class FileSystemSession(ServerSideSession):
    pass


class MongoDBSession(ServerSideSession):
    pass


class SqlAlchemySession(ServerSideSession):
    pass


class SessionInterface():

    def _generate_sid(self):
        return str(uuid4())

    def _get_signer(self, app):
        if not app.secret_key:
            return None
        return Signer(app.secret_key, salt='starlette-session',
                      key_derivation='hmac')


class NullSessionInterface(SessionInterface):
    """Used to open a :class:`flask.sessions.NullSession` instance.
    """

    def open_session(self, app, request):
        return None



class MongoDBSessionInterface(SessionInterface):
    """A Session interface that uses mongodb as backend.

    .. versionadded:: 0.2
        The `use_signer` parameter was added.

    :param client: A ``pymongo.MongoClient`` instance.
    :param db: The database you want to use.
    :param collection: The collection you want to use.
    :param key_prefix: A prefix that is added to all MongoDB store keys.
    :param use_signer: Whether to sign the session id cookie or not.
    :param permanent: Whether to use permanent session or not.
    """

    serializer = JSONSerializer()
    session_class = MongoDBSession

    def __init__(self, client, db, collection, key_prefix, use_signer=False,
                 permanent=True):

        cl = dataBase.motorConf("client","write")
        self.client = client
        self.store = cl[db][collection]
        self.key_prefix = key_prefix
        self.use_signer = use_signer
        self.permanent = permanent
        self.has_same_site_capability = hasattr(self, "get_cookie_samesite")

    def open_session(self, app, request):
        sid = request.session.get(config('SESSION_COOKIE_NAME'))
        if not sid:
            sid = self._generate_sid()
            return self.session_class(sid=sid, permanent=self.permanent)
        if self.use_signer:
            signer = self._get_signer(app)
            if signer is None:
                return None
            try:
                sid_as_bytes = signer.unsign(sid)
                sid = sid_as_bytes.decode()
            except BadSignature:
                sid = self._generate_sid()
                return self.session_class(sid=sid, permanent=self.permanent)

        store_id = self.key_prefix + sid
        document = self.store.find_one({'id': store_id})
        if document and document.get('expiration') <= datetime.utcnow():
            # Delete expired session
            self.store.remove({'id': store_id})
            document = None
        if document is not None:
            try:
                val = document['val']
                data = self.serializer.loads(want_bytes(val))
                return self.session_class(data, sid=sid)
            except:
                return self.session_class(sid=sid, permanent=self.permanent)
        return self.session_class(sid=sid, permanent=self.permanent)

    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        path = self.get_cookie_path(app)
        store_id = self.key_prefix + session.sid
        if not session:
            if session.modified:
                self.store.remove({'id': store_id})
                response.delete_cookie(config('SESSION_COOKIE_NAME'),
                                       domain=domain, path=path)
            return

        conditional_cookie_kwargs = {}
        httponly = self.get_cookie_httponly(app)
        secure = self.get_cookie_secure(app)
        if self.has_same_site_capability:
            conditional_cookie_kwargs["samesite"] = self.get_cookie_samesite(app)
        expires = self.get_expiration_time(app, session)
        val = self.serializer.dumps(dict(session))
        self.store.update({'id': store_id},
                          {'id': store_id,
                           'val': val,
                           'expiration': expires}, True)
        if self.use_signer:
            session_id = self._get_signer(app).sign(want_bytes(session.sid))
        else:
            session_id = session.sid
        response.set_cookie(config('SESSION_COOKIE_NAME'), session_id,
                            expires=expires, httponly=httponly,
                            domain=domain, path=path, secure=secure,
                            **conditional_cookie_kwargs)
