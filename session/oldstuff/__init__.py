# -*- coding: utf-8 -*-
"""
    starlette_session
    ~~~~~~~~~~~~~

    Adds server session support to your application.

    :copyright: (c) 2014 by Shipeng Feng.
    :copyright: (c) 2020 by Kroket Ltd.
    :license: BSD, see LICENSE for more details.
"""

__version__ = '2.0.0'

import os
from decouple import config

from starlette.applications import Starlette
from starlette.types import ASGIApp, Message, Receive, Scope, Send
import asyncio

from .sessions import (
    MongoDBSessionInterface,
    NullSessionInterface,
    SessionInterface
)


class Session(object):
    """This class is used to add Server-side Session to one or more ASGIApp
    applications.

    There are two usage modes.  One is initialize the instance with a very
    specific ASGIApp application::

        app = ASGIApp(__name__)
        Session(app)

    The second possibility is to create the object once and configure the
    application later::

        sess = Session()

        def create_app():
            app = ASGIApp(__name__)
            sess.init_app(app)
            return app

    By default ASGIApp-Session will use :class:`NullSessionInterface`, you
    really should configure your app to use a different SessionInterface.

    .. note::

        You can not use ``Session`` instance directly, what ``Session`` does
        is just change the :attr:`~quart.ASGIApp.session_interface` attribute on
        your ASGIApp applications.
    """

class ASGISessionMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        async def send_wrapper(message: Message) -> None:
            
            # ... Do something
            await send(message)

        await self.app(scope, receive, send_wrapper)



"""Support cookie-encrypted sessions for ASGI applications."""

from __future__ import annotations

import sys
from base64 import urlsafe_b64decode, urlsafe_b64encode
from http import cookies
from typing import TYPE_CHECKING, Any, Dict, Optional, Union, cast

from db.database import dataBase
import asyncio

from asgi_tools import Request, Response
from asgi_tools._compat import json_dumps, json_loads
from asgi_tools.middleware import BaseMiddeware

if TYPE_CHECKING:
    from asgi_tools.types import TJSON, TASGIApp, TASGIReceive, TASGIScope, TASGISend

Fernet: Any
InvalidToken: Any

try:
    from cryptography.fernet import Fernet, InvalidToken
except ImportError:
    Fernet, InvalidToken = None, None


jwt: Any

try:
    import jwt
except ImportError:
    jwt = None


__all__ = "SessionMiddleware", "Session", "SessionJWT", "SessionFernet"


class SessionMiddleware(ASGISessionMiddleware):
    """Support sessions."""

    def __init__(
        self,
        app: TASGIApp,
        secret_key: Optional[str] = None,
        *,
        session_type: str = "mongodb",
        cookie_name: str = "session",
        max_age: int = 360,
        samesite: str = "lax",
        secure: bool = False,
    ):
        """Init the middleware."""
        super(SessionMiddleware, self).__init__(app)
        assert secret_key, "secret_key is required"
        self.secret_key = secret_key
        self.session_name = session_name
        self.session_type = session_type

        self.session_params: Dict[str, Any] = {"path": "/"}
        if max_age:
            self.session_params["max-age"] = max_age
        if secure:
            self.session_params["secure"]: bool = False
        if sys.version_info >= (3, 8) and samesite:  # XXX: Python 3.7
            self.session_params["samesite"] = samesite
        if domain:
            self.session_params["domain"] = domain

    async def __process__(
        self, scope: Union[TASGIScope, Request], receive: TASGIReceive, send: TASGISend,
    ):
        """Load/save the sessions."""
        # Support asgi_tools.RequestMiddleware
        if isinstance(scope, Request):
            request = scope
        else:
            request = scope.get("request") or Request(scope, receive, send)

        session = self.init_session(request.session.get(self.session_name))
        scope["session"] = session

        # Common ASGI Applications
        def send_wrapper(message):
            """Inject sessions cookie."""
            if session.modified and message["type"] == "http.response.start":
                client = dataBase.motorConf("client",self.method)
                message["headers"].append(
                    (
                        b"Set-Cookie",
                        session.data(self.session_name, self.session_params).encode(),
                    ),
                )

            return send(message)

        # Support ASGI-Tools Responses
        response = await self.app(scope, receive, send_wrapper)
        if response and isinstance(response, Response) and session.modified:
            response.headers["Set-Cookie"] = session.cookie(
                self.cookie_name, self.session_params,
            )

        return response

    def init_session(self, token: Optional[str] = None, session_id: Optional[str] = None) -> Session:
        if self.session_type == "jwt":
            return SessionJWT(token, secret=self.secret_key)

        if self.session_type == "fernet":
            return SessionFernet(token, secret=self.secret_key)

        if self.session_type == "mongodb":
            session_
            return SessionMongoDB

        return Session(token)


class Session(dict):
    """Base4 session (not encrypted!)."""

    modified = False

    def __init__(self, value: Optional[str] = None, **payload):
        """Initialize the container."""
        if value:
            self.update(self.decode(value))

        if payload:
            self.update(payload)

    def __setitem__(self, name: str, value: TJSON):
        """Store the value and check that the session is pure."""
        self.modified = self.get(name) != value
        dict.__setitem__(self, name, value)

    def __delitem__(self, name: str):
        """Delete the value and check that the session is pure."""
        self.modified = name in self
        dict.__delitem__(self, name)

    def cookie(self, cookie_name: str, session_params: Dict) -> str:
        """Render the data as a cookie string."""
        morsel: cookies.Morsel = cookies.Morsel()
        value = self.encode()
        morsel.set(cookie_name, value, value)
        for k in session_params:
            morsel[k] = session_params[k]
        return morsel.OutputString()

    def clear(self) -> None:
        self.modified = bool(self)
        return dict.clear(self)

    def pop(self, name: str, default=None) -> TJSON:
        self.modified = bool(self)
        return dict.pop(self, name, default)

    def update(self, value):
        self.modifield = bool(value)
        return dict.update(self, value)

    def encode(self) -> str:
        payload = json_dumps(self)
        return urlsafe_b64encode(payload).decode()

    def decode(self, token: str, *, silent: bool = True) -> Dict:
        try:
            payload = urlsafe_b64decode(token)
        except ValueError:
            if silent:
                return {}
            raise
        else:
            return json_loads(payload)


class SessionJWT(Session):
    """Keep/update sessions data."""

    def __init__(self, *args, secret=None, **kwargs):
        if jwt is None:
            raise RuntimeError("Install jwt package to use JWT sessions.")

        if not secret:
            raise ValueError("SessionJWT.secret is required.")

        self.secret = secret
        super(SessionJWT, self).__init__(*args, **kwargs)

    def encode(self) -> str:
        """Encode the session's data."""
        token = jwt.encode(self, key=self.secret, algorithm="HS256")
        # Support JWT<2 (Remove me after 2022-01-01)
        if isinstance(token, bytes):
            return token.decode()
        return token

    def decode(self, token, *, silent=True) -> Dict:
        try:
            payload = jwt.decode(token, key=self.secret, algorithms=["HS256"])
            return cast(Dict, payload)
        except jwt.DecodeError:
            if not silent:
                raise

        return {}


class SessionFernet(Session):
    """Keep/update sessions data."""

    def __init__(self, *args, secret=None, **kwargs):
        if Fernet is None:
            raise RuntimeError("Install cryptography package to use fernet sessions.")

        if not secret:
            raise ValueError("SessionFernet.secret is required.")

        if len(secret) != 32:
            secret = secret[:32]
            secret += "=" * (32 - len(secret) % 32)

        self.secret = urlsafe_b64encode(secret.encode())
        self.f = Fernet(self.secret)
        super(SessionFernet, self).__init__(*args, **kwargs)

    def encode(self) -> str:
        """Encode the session's data."""
        payload = json_dumps(self)
        return self.f.encrypt(payload).decode()

    def decode(self, token, *, silent=True) -> Dict:
        try:
            payload = self.f.decrypt(token.encode())
            return json_loads(payload)
        except InvalidToken:
            if not silent:
                raise

        return {}


class SessionMongoDB(Session):

    def __init__(self, *args, **kwargs):
        self.method = self.kwargs.pop('method')
        self.db = self.kwargs.pop('db')
        self.col = self.kwargs.pop('col')
        self.session_key = self.kwargs.pop('session_id')
        
        client = dataBase.motorConf("client", self.method)
        col = client[self.db][self.col]

    async def get(self, key: str, **kwargs: dict) -> Optional[dict]:  # pragma: no cover
        value = await self.mongodb.get(key.encode(), **kwargs)
        return _loads(value) if value else None

    async def set(
        self, key: str, value: dict, exp: Optional[int] = None, **kwargs: dict
    ) -> Optional[str]:  # pragma: no cover
        return await self.memcache.set(key.encode(), _dumps(value), exptime=exp, **kwargs)

    async def delete(self, key: str, **kwargs: dict) -> Any:  # pragma: no cover
        return await self.memcache.delete(key.encode(), **kwargs)

    async def update(self, key: str, value: dict)
                  
        
# import os

# from .sessions import NullSessionInterface, RedisSessionInterface, \
#     MemcachedSessionInterface, FileSystemSessionInterface, \
#     MongoDBSessionInterface, SqlAlchemySessionInterface

# __version__ = '0.5.0'


# class Session(object):
#     """This class is used to add Server-side Session to one or more Flask
#     applications.

#     There are two usage modes.  One is initialize the instance with a very
#     specific Flask application::

#         app = Flask(__name__)
#         Session(app)

#     The second possibility is to create the object once and configure the
#     application later::

#         sess = Session()

#         def create_app():
#             app = Flask(__name__)
#             sess.init_app(app)
#             return app

#     By default Flask-Session will use :class:`NullSessionInterface`, you
#     really should configurate your app to use a different SessionInterface.

#     .. note::

#         You can not use ``Session`` instance directly, what ``Session`` does
#         is just change the :attr:`~flask.Flask.session_interface` attribute on
#         your Flask applications.
#     """

#     def __init__(self, app=None):
#         self.app = app
#         if app is not None:
#             self.init_app(app)

#     def init_app(self, app):
#         """This is used to set up session for your app object.

#         :param app: the Flask app object with proper configuration.
#         """
#         app.session_interface = self._get_interface(app)

#     def _get_interface(self, app):
#         config = app.config.copy()
#         config.setdefault('SESSION_TYPE', 'null')
#         config.setdefault('SESSION_PERMANENT', True)
#         config.setdefault('SESSION_USE_SIGNER', False)
#         config.setdefault('SESSION_KEY_PREFIX', 'session:')
#         config.setdefault('SESSION_REDIS', None)
#         config.setdefault('SESSION_MEMCACHED', None)
#         config.setdefault('SESSION_FILE_DIR',
#                           os.path.join(os.getcwd(), 'flask_session'))
#         config.setdefault('SESSION_FILE_THRESHOLD', 500)
#         config.setdefault('SESSION_FILE_MODE', 384)
#         config.setdefault('SESSION_MONGODB', None)
#         config.setdefault('SESSION_MONGODB_DB', 'flask_session')
#         config.setdefault('SESSION_MONGODB_COLLECT', 'sessions')
#         config.setdefault('SESSION_SQLALCHEMY', None)
#         config.setdefault('SESSION_SQLALCHEMY_TABLE', 'sessions')

#         if config['SESSION_TYPE'] == 'redis':
#             session_interface = RedisSessionInterface(
#                 config['SESSION_REDIS'], config['SESSION_KEY_PREFIX'],
#                 config['SESSION_USE_SIGNER'], config['SESSION_PERMANENT'])
#         elif config['SESSION_TYPE'] == 'memcached':
#             session_interface = MemcachedSessionInterface(
#                 config['SESSION_MEMCACHED'], config['SESSION_KEY_PREFIX'],
#                 config['SESSION_USE_SIGNER'], config['SESSION_PERMANENT'])
#         elif config['SESSION_TYPE'] == 'filesystem':
#             session_interface = FileSystemSessionInterface(
#                 config['SESSION_FILE_DIR'], config['SESSION_FILE_THRESHOLD'],
#                 config['SESSION_FILE_MODE'], config['SESSION_KEY_PREFIX'],
#                 config['SESSION_USE_SIGNER'], config['SESSION_PERMANENT'])
#         elif config['SESSION_TYPE'] == 'mongodb':
#             session_interface = MongoDBSessionInterface(
#                 config['SESSION_MONGODB'], config['SESSION_MONGODB_DB'],
#                 config['SESSION_MONGODB_COLLECT'],
#                 config['SESSION_KEY_PREFIX'], config['SESSION_USE_SIGNER'],
#                 config['SESSION_PERMANENT'])
#         elif config['SESSION_TYPE'] == 'sqlalchemy':
#             session_interface = SqlAlchemySessionInterface(
#                 app, config['SESSION_SQLALCHEMY'],
#                 config['SESSION_SQLALCHEMY_TABLE'],
#                 config['SESSION_KEY_PREFIX'], config['SESSION_USE_SIGNER'],
#                 config['SESSION_PERMANENT'])
#         else:
#             session_interface = NullSessionInterface()

#         return session_interface