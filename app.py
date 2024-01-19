from decouple import config
from asgi_logger import AccessLoggerMiddleware

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette_wtf import CSRFProtectMiddleware

from typing import Optional
import session
from session import SessionMiddleware

import asyncio
import aiomcache
from session_data import (
    view_session,
    clear_session,
    session,
    setup_session
)

from session.backends import (
    AioMemcacheSessionBackend,
    AioRedisSessionBackend,
    BackendType,
    MemcacheSessionBackend,
    RedisSessionBackend,
)
from session.interfaces import ISessionBackend


from starlette.requests import Request, HTTPConnection
from starlette.routing import Route, Mount
from exc import (
    unhandled_exception_handler,
    http_exception_handler,
    page_not_found_exception_handler,
    server_error_exception_handler,
)

# from .stores import MongoDBStore
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
import aiomcache

from starlette.types import Receive, Scope, Send, Scope as scope
from starlette.applications import Starlette
from starlette.exceptions import HTTPException

from starlette.responses import JSONResponse, HTMLResponse
from starlette.staticfiles import StaticFiles

from routes import (
    login,
    index,
    register,
    logout,
    profile,
    clean,
    check,
    changepass
)
from forms import User


memcache_client = aiomcache.client.Client(host="dockerswarm-memcached-1", port=11211)
secret = config("SESS_SECRET_KEY")
env = Environment(
    loader=FileSystemLoader("templates/", encoding="utf-8"),
    auto_reload=True,
    enable_async=True,
)


HTML_500_PAGE = env.get_template("HTML_500_PAGE")
HTML_404_PAGE = env.get_template("HTML_404_PAGE")


async def not_found(request: Request, exc: HTTPException):
    return HTMLResponse(content=HTML_404_PAGE, status_code=exc.status_code)


async def server_error(request: Request, exc: HTTPException):
    return HTMLResponse(content=HTML_500_PAGE, status_code=exc.status_code)


async def http_exception(request: Request, exc: HTTPException):
    return JSONResponse(
        {"detail": exc.detail}, status_code=exc.status_code, headers=exc.headers
    )


headers = {"Cache-Control": "public, max-age: 1600"}

routes = [
    Route("/", index, methods=["GET"], name="index"),
    Route("/users/{username}", methods=["GET", "POST"], endpoint=User),
    Mount("/static", StaticFiles(directory="static"), name="static"),
    Mount("/images", StaticFiles(directory="images"), name="images"),
    Mount("/style", StaticFiles(directory="style"), name="style"),
    Route("/login", login, methods=["GET", "POST", "HEAD"], name="login"),
    Route("/changepass", changepass, methods=["GET", "POST", "HEAD"], name="changepass"),
    Route("/logout", logout, methods=["GET"], name="logout"),
    Route("/profile", profile, methods=["GET", "POST"], name="profile"),
    Route("/register", register, methods=["GET", "POST"], name="register"),
    Route("/check", check, methods=["GET", "POST", "HEAD"], name="check"),
    Route("/session", session, methods=["GET", "POST", "HEAD"], name="session"),
    Route(
        "/clear_session",
        endpoint=clear_session
        ),
    Route(
        "/view_session",
        endpoint=view_session
        ),
    Route(
        "/setup_session",
        setup_session,
        methods=["GET", "POST", "HEAD"],
        name="setup_session"
    ),
    # Route(
    #     "/build_welcome",
    #     build_welcome,
    #     methods=["GET", "POST", "HEAD"],
    #     name="build_welcome"
    # ),
    #    Route("/update_session", endpoint=update_session),
    Route("/clean", clean, methods=["GET"], name="clean"),
]


middleware = [
    # Middleware(SessionMiddleware,
    #     lifetime = 360,
    #     cookie_https_only=False,  # Key for cookie signature
    #     store = MongoDBStore
    # ),
    # Middleware(SessionAutoloadMiddleware
    # ),
    Middleware(CSRFProtectMiddleware, csrf_secret=secret, enabled=False),
    Middleware(AccessLoggerMiddleware),
    Middleware(
        SessionMiddleware,
        secret_key=secret,
        max_age=360,
        cookie_name="session",
        backend_type=BackendType.aioMemcache,
        backend_client=memcache_client,
    ),
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["GET", "POST", "HEAD", "OPTIONS"],
        allow_headers=["*"],
    ),
]


class App(Starlette):
    def __init__(
        self,
        debug: bool = False,
        routes: Optional[list] = None,
        middleware: Optional[list] = None,
    ) -> None:
        if routes is None:
            routes = []
            routes.append(list(routes))
        if middleware is None:
            middleware = []
            middleware.append(list(middleware))
        super().__init__(debug, routes, middleware)
        self.add_exception_handler(418, http_exception_handler)
        self.add_exception_handler(404, page_not_found_exception_handler)
        self.add_exception_handler(500, server_error_exception_handler)
        self.add_exception_handler(502, unhandled_exception_handler)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "http":
            return await super().__call__(scope, receive, send)


app = App(debug=True, routes=routes, middleware=middleware)


# @app.on_event("startup")
# async def on_startup():
#     rcli = dataBase.pyMongoConf('','read')
#     wcli = dataBase.pyMongoConf('','write')
#     dbr = rcli['eCom']
#     dbw = wcli['eCom']

#     try:
#         wcol = dbw['userData']
#         rcol = dbr['userData']
#     finally:
#         async def close():
#             dataBase.close()


# async def app(scope, receive, send):

#     """Read session and get the current user data from it or from request query."""
#     # The middleware puts a session into scope['session]
#     session = scope['session']

#     status, headers = 200, []
#     if scope['query_string']:
#         # Store any information inside the session
#         session['user'] = scope['query_string'].decode()
#         status, headers = 307, [(b"location", b"/")]

#     # Read a stored info from the session
#     user = (session.get('user') or 'anonymous').title().encode()

#     await send({"type": "http.response.start", "status": status, "headers": headers})
#     await send({"type": "http.response.body", "body": b"Hello %s" % user})


# ## scope={'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.3'}, 'http_version': '1.0', 'server': None, 'client': None, 'scheme': 'http', 'root_path': '/', 'headers': '<...>', 'state': {}, 'method': 'GET', 'path': '/login', 'raw_path': b'/login', 'query_string': b''}
# app = App(routes=routes, middleware=middleware, exception_handlers=exception_handlers)


#     async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
#         if self.root_path:
#             scope["root_path"] = self.root_path
#         await super().__call__(scope, receive, send)

#     async def get(self, Scope, Receive, Send):
#         self.scope = Scope
#         self.receive = Receive
#         self.send = Send
#         app = await App.__init__("app", scope=self.scope, receive=self.receive, send=self.send)
#         app.add_middleware(middleware)
#         app.add_route(routes)
#         app.add_exception_handlers(exception_handlers)
#         return app
# async def lifespan(app):
#     u = UserData
#     r_db = await u._getDb("read")
#     w_db = await u._getDb("write")
#     print("Run at startup!")
#     yield
#     print("Run on shutdown!")
#     r_db.close()
#     w_db.close()


# app.add_middleware(ASGI2Middleware(app: Starlette))
# app.add_middleware(SessionMiddleware.setup(session_type='jwt', secret_key=sk))
# cookie_https_only=False,
# cookie_same_site='lax',
# cookie_domain='nix.onion',
# serializer=JsonSerializer()

################################################################################################
#
#
# OLD ITERATIONS OF CODE
#
################################################################################################

# app.add_middleware(
#     SessionMiddleware,
#     secret_key=sk,
#     cookie_name='__cookie',
#     https_only=False,
#     max_age=360,
#     same_site='lax',
#     domain='nix.onion',
#     custom_session_backend=MemcacheSessionBackend,
#     backend_type=BackendType.memcache,
#     backend_client=Memcache
# )

# memcache_client = aiomcache.Client("dockerswarm-memcached-1", "11211")


# async  def create_app_instance():
#     app = await App()
# # memcache_client = aiomcache.Client(
# #     host="dockerswarm-memcached-1", port="11211", pool_size=6)
# app.add_middleware(CSRFProtectMiddleware, csrf_secret=sk, enabled=True, csrf_headers=[
#              "X-CSRF-Token", "X-CSRFToken"], csrf_time_limit=300, csrf_ssl_strict=False)
# app.add_middleware(SessionMiddleware, secret_key=sk, cookie_name="_cssid", domain="nix.onion",
#                    max_age=360, backend_type=BackendType.aioMemcache, backend_client='memcache_client', https_only=False, custom_session_backend=AioMemcacheSessionBackend(memcache=memcache_client))
# # app.add_middleware(CORSMiddleware,  allow_origins=['*'], allow_headers=['*'])
# app.add_middleware(ProxyHeadersMiddleware, trusted_hosts=["*"])
# app.add_middleware(MessageLoggerMiddleware)
# app.add_middleware(ExtraResponseHeadersMiddleware,
#                   headers={'Cache-Control': 'no-store',
#                            'X-CSRF-Token': 'csrf_token'
#                           })
# app.add_middleware(ASGI2Middleware)
# app.add_middleware(CurrentRequestMiddleware)
# app.add_middleware(AuthlibMiddleware, secret_key=sk)
# async def app():
#     app = await self.app(scope, receive, send)
#     assert scope['type'] == 'http'
#     request = Request(scope, receive)
#     content = '%s %s' % (request.method, request.url.path)
#     headers = '%s' % (request.headers)
#     body = await request.body()
#     response = Response(content, media_type='text/plain')
#     return app
# #     await response(scope, receive, send)\

#     app = await create_app()
#     assert scope['type'] == 'http'
#     request = Request(scope, receive)
#     content = '%s %s' % (request.method, request.url.path)
#     headers = '%s %s' % (request.headers)
#     body = await request.body()
#     response = Response(content, media_type='text/plain')


# config = uvicorn.Config(
#     "app:app",
#     log_level="trace",
#     uds="/tmp/ecommerce.sock",
#     #     reload=True,l
#     loop="uvloop",
#     #factory=True,
#     workers=4,
#     http='httptools',
#     interface='auto',
#     use_colors=True,
#     root_path="/"

# )

# if __name__ == "__main__":
#     server = uvicorn.Server(config)
#     server.run()
# async def lifespan(app):
#     async with u._getDb("read") as db:
#         print("Run at startup!")
#         yield
#         print("Run on shutdown!")
#     db.close()
# style = request.url_for(name='style', path='/style', methods=['GET'])
# static = request.url_for(name='static', path='/static', methods=['GET'])

# async def __call__.super(self, debug: bool = False, routes: Optional[list], middleware: Optional[list], exception_handlers, on_startup):
#     self.middleware = middleware
#     self.routes = routes
#     self.exception_handlers = exception_handlers
#     self.on_startup = [startup]
#     return self


# app = Starlette(
#     routes=routes,
#     exception_handlers=exception_handlers,
#     debug=True,
#     #on_startup=[startup]
# )

# app.add_middleware(Middleware(CSRFProtectMiddleware(app=Starlette, csrf_secret=sk, csrf_headers=['X-CSRFToken', 'X-CSRF-Token'], csrf_ssl_strict=False, enabled=False)))


# app.add_middleware(
#             CORSMiddleware,
#             allow_origins=["*"],
#             allow_methods=["GET", "POST", "HEAD", "OPTIONS"],
#             allow_headers=["*"]
#                 # "access-control-allow-origin",
#                 # "authorization"
#                 # "content-type",
#                 # "X-CSRFToken",
#                 # "X-CSRF-Token"
# )
