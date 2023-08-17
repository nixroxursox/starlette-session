import asyncio
import uvloop
import uvicorn
from starlette.applications import Starlette
from starlette.middleware.sessions import SessionMiddleware
import httptools
import starlette
import starlette_wtf
import middleware
from starlette_wtf import CSRFProtectMiddleware, StarletteForm, csrf_protect
from starlette.requests import  Request as request
from starlette.responses import Response as response
from starlette.responses import JSONResponse, HTMLResponse, RedirectResponse, PlainTextResponse
from starlette.middleware import Middleware
from starlette.routing import Route, Mount, Router
from decouple import config
from jinja2 import Template
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from starlette.templating import Jinja2Templates
from wtforms import StringField
from wtforms.validators	import DataRequired
from routes import homepage
from forms import User

env = Environment(loader=FileSystemLoader('templates'))
templates = Jinja2Templates(env=env)
sk = config('SECRET_KEY')


middleware = [
    Middleware(CSRFProtectMiddleware, csrf_secret=sk),
    Middleware(SessionMiddleware, secret_key=sk)
]

routes = [
    Route('/', homepage, methods=['GET','POST'], name = 'homepage'),
    Route("/{username}", User)
]


app = Starlette(
    routes=routes,
    middleware=middleware,
    debug=True
)

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
#     await response(scope, receive, send)


config = uvicorn.Config(
     "app:app",
     log_level="debug",
     uds="/tmp/ecommerce.sock"
#     reload=True,
#     loop="uvloop",
#     factory=True,
#     workers=8,
#     http='httptools'
)
        
if __name__ == "__main__":
    server = uvicorn.Server(config)
    server.run()
