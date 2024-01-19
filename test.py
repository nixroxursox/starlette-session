import json
import time
from db.database import dataBase
from accounts import UserData as u
import pprint
from nacl import pwhash
import jinja2
import aiomcache
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
from forms import LoginForm, RegistrationForm
from starlette_wtf.form import StarletteForm, StarletteRequest
from starlette.requests import Request
from wtforms.validators import length
from starlette.requests import Request
from starlette.datastructures import Headers
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.requests import Request, HTTPConnection
from starlette.responses import HTMLResponse, RedirectResponse, Response
from starlette.routing import Route
import uvicorn

from app import App, middleware, routes, env, secret, not_found, server_error, http_exception
app = App(debug=True, routes=routes, middleware=middleware)

import asyncio
import aiomcache

user = '67test'
pw = 'changeMe'
pi = '102020202'
nname = 'therealnix'
st = 'boring personal statement'
pgp = 'templkeyplacement'


client = dataBase.pyMongoConf('client', 'read')
db = client['eCom']
col = db['userData']


v = u.py_v_Pass(user, pw)
v1 = u.py_v_Pin(user, pi)


env = Environment(
    loader=FileSystemLoader("templates/", encoding="utf-8"), auto_reload=True, enable_async=True)

form = RegistrationForm(StarletteRequest)
title = "Register"
context = {'request': StarletteRequest, 'form': form, 'title': title}
template = env.get_template('auth/formfill.html')
html = template.render(context=context, form=form, title=title)


# newu = u.py_createUser(user,pw,pi,nname,st,pgp)


async def homepage(request: Request) -> Response:
    """Access this view (GET "/") to display session contents."""
    return HTMLResponse(
        """
    <form method="post" action="/login">
    <label> Username <input type="text" name="username"> </label>
    <button type="submit">Sign in</button>
    </form>
    <a href="/profile">My profile</a>
    """
    )


async def login(request: Request) -> Response:
    form_data = await request.form()
    username = form_data["username"]
    request.session["username"] = username
    regenerate_session_id(request)
    return RedirectResponse("/profile", 302)


async def logout(request: Request) -> Response:
    request.session.clear()
    return RedirectResponse("/", 302)


async def profile(request: Request) -> Response:
    username = request.session.get("username")
    if not username:
        return RedirectResponse("/", 302)
    return HTMLResponse(
        """
    <p>Hi, {username}!</p>
    <form method="post" action="/logout">
    <button type="submit">logout</button>
    </form>
        """.format(
            username=username
        )
    )


async def hello_aiomcache():
    mc = aiomcache.Client("dockerswarm-memcached-1", 11211)
    await mc.set(b"some_key", b"Some value")
    value = await mc.get(b"some_key")
    print(value)
    values = await mc.multi_get(b"some_key", b"other_key")
    print(values)
    await mc.delete(b"another_key")

asyncio.run(hello_aiomcache())


def build_request(
    method: str = "GET",
    server: str = "nix.onion",
    path: str = "/session",
    headers: dict = None,
    body: str = None,
    session: dict = None
) -> Request:
    if headers is None:
        headers = {
            "cache-control": "no-cache",
            "host": "nix.onion",
            "accept": "application/json",
            "X-Forwarded-For": "192.168.32.1",
            "X-Real-IP": "10.40.0.1"
        }
    if session is None:
        session = {
            "username": "696969",
            "x-session-id": "9348d82528bacbe4eb36e862059a5359"
        }
    request = Request(
        {
            "type": "http",
            "path": path,
            "headers": Headers(headers).raw,
            "http_version": "1.1",
            "method": method,
            "scheme": "http",
            "client": ("127.0.0.1", 80),
            "server": (server, 8082),
        }
    )
    # if body:
    #     async def request_body():
    #         return body

    #     request.body = request_body
    return request


def build_scope():
    scope = {
        "type": "http",
        "http_version": "1.1",
        "method": "GET",
        "scheme": "http",
        "path": "/",
        "query_string": b"search=red+blue&maximum_price=20",
        "headers": [
            (b"host", b"www.example.org"),
            (b"accept", b"application/json"),
            (b"X-Forwarded-For", b"192.168.32.1"),
            (b"X-Real-IP", b"192.168.32.2")
        ],
        "client": ("134.56.78.4", 1453),
        "server": ("www.example.org", 443)
    }
    return scope


scope = build_scope()
# serializer = JsonSerializer()
# store = MongoDBStore()
connection = HTTPConnection(scope)


async def hello_aiomcache():
    # memcache_client = aiomcache.Client("dockerswarm-memcached-1", 11211)
    mc = aiomcache.Client("dockerswarm-memcached-1", 11211)
    await mc.set(b"some_key", b"Some value")
    await mc.set(b"some_other_key", b"Some other value")
    value = await mc.get(b"some_key")
    values = await mc.multi_get(b"some_key", b"other_key")
    print(values)
    await mc.delete(b"another_key")


#session_id = generate_session_id()
lifetime = 360
ttl = 10
data = {}

scope = build_scope()
request = build_request()


app = App(middleware=middleware, routes=routes, debug=True)
session_id = '9348d82528bacbe4eb36e862059a5359'


# handler = SessionHandler(connection, session_id, store, lifetime)
# connection.scope["session_handler"] = handler

data = store.read(     # this finds the session_id in the database and also lifetime
    session_id,  # get session_id from dataBase
    lifetime,  # get lifetime from dataBase
)


# initially_empty = len(connection.session) == 0
# remaining_time = get_session_remaining_seconds(connection)


# creates  metadata for session and adds lifetime, created and last access
metadata = {"lifetime": lifetime,
            "created": time.time(), "last_access": time.time()}
data.update(metadata)
# mdata = self.store.update_metadata("meta", self.metadata["lifetime"], self.metadata["created"], self.metadata["last_access"])
# we're still  in existing session and now getting the metadata info by popping data - this will return lifetime, created, and last_access
metadata.update(data.pop("__metadata__", {}))
# force update  - this updates last access to now
metadata.update({"last_access": time.time()})
# type: ignore[assignment]   #takes metadata and scopes it into this class so we can use it in other functions )
metadata = metadata


connection.scope["session"] = {}
# request.session is created here - this is  a "NEW SESSION"
connection.session.update({"X-Session-ID": session_id}
                          )  # request.session is populated here with data from data - this adds existing data to the new session \
for k, v in data.items():
    connection.session.update({"k": v})

connection.session

# this empties session - no idea why
initially_empty = len(connection.session) == 0
remaining_time = get_session_remaining_seconds(connection)
