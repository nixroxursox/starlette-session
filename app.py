from decouple import config
from jinja2.loaders import FileSystemLoader
from starlette.applications import Starlette
from starlette.datastructures import Headers
from starlette.exceptions import HTTPException
from starlette.requests import Request, Request as request
from starlette.responses import HTMLResponse, JSONResponse
from starlette.responses import Response, Response as response
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette_session import SessionMiddleware, AioMemcacheSessionBackend
from starlette_session.backends import BackendType
from starlette.types import ASGIApp, Message, Scope, Receive, Send
from typing import Sequence
import aiomcache
import jinja2
import uvicorn
import gunicorn
from routes import login, index, create_account, setup_session, view_session, clear_session, register
from forms import User

# style = request.url_for(name='style', path='/style', methods=['GET'])
# static = request.url_for(name='static', path='/static', methods=['GET'])

env = jinja2.Environment(loader=FileSystemLoader(
    "templates/", encoding='utf8', followlinks=True), auto_reload=True)
sk = config('SECRET_KEY')


# memcache_client = aiomcache.Client("dockerswarm-memcached-1", "11211")
# middleware = [
#     Middleware(SessionMiddleware, secret_key=sk, cookie_name="_cook", max_age=360, backend_type=BackendType.aioMemcache, backend_client=memcache, custom_session_backend=AioMemcacheSessionBackend)
# ]


async def not_found(request: Request, exc: HTTPException):
    return HTMLResponse(content=HTML_404_PAGE, status_code=exc.status_code)


async def server_error(request: Request, exc: HTTPException):
    return HTMLResponse(content=HTML_500_PAGE, status_code=exc.status_code)


async def http_exception(request: Request, exc: HTTPException):
    return JSONResponse(
        {"detail": exc.detail},
        status_code=exc.status_code,
        headers=exc.headers
    )

exception_handlers = {
    HTTPException: http_exception,
    404: not_found,
    500: server_error
}

headers = {
    'Cache-Control': 'public, max-age: 1600'
}

routes = [
    Route('/', index, methods=['GET'], name='index'),
    Route('/users/{username}', methods=['GET', 'POST'], endpoint=User),
    Mount('/static', StaticFiles(directory='static'), name='static'),
    Mount('/images', StaticFiles(directory='images'), name='images'),
    Mount('/style', StaticFiles(directory='style'), name='style'),
    Route('/login', login, methods=['GET', 'POST'], name='login'),
    Route('/create-account', create_account,
          methods=['GET', 'POST'], name='create_account'),
    Route('/profile', methods=['GET', 'POST'], endpoint='Profile'),
    Route('/setup_session', endpoint=setup_session),
    Route('/clear_session', endpoint=clear_session),
    Route('/view_session', endpoint=view_session),
    Route('/register', register, methods=['GET', 'POST'], name='register')
]



# class App(Starlette):
#     async def __init__(self, routes, middleware, exception_handlers):
#         self,
#         self.middleware = middleware
#         self.routes = routes
#         self.exception_handlers = exception_handlers


#         await super().__init__(
#             self,
#             routes,
#             exception_handlers,
#             middleware
#         )

#     async def __call__(self, routes, exception_handlers, middleware):
#         self.scope = Scope
#         self.routes: str = routes
#         self.middleware = middleware
#         self.exception_handlers = exception_handlers
#         await super().__call__(routes, exception_handlers, middleware)
        
        
        
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

app = Starlette(
    routes=routes,
    exception_handlers=exception_handlers,
    debug=True
)

memcache = aiomcache.Client(
    host="dockerswarm-memcached-1", port="11211", pool_size=6)

app.add_middleware(
    SessionMiddleware,
    secret_key=sk,
    cookie_name="_sess",
    backend_type=BackendType.aioMemcache,
    backend_client=memcache
)
# async  def create_app_instance():
#     app = await App()
# # memcache_client = aiomcache.Client(
# #     host="dockerswarm-memcached-1", port="11211", pool_size=6)
#app.add_middleware(CSRFProtectMiddleware, csrf_secret=sk, enabled=True, csrf_headers=[
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
# app.add_middleware(ASGI2Middleware, app=app)
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
