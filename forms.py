from jinja2 import Template
from starlette_wtf import StarletteForm, CSRFProtectMiddleware, csrf_protect
from wtforms import StringField
from wtforms.validators	import DataRequired
from starlette.applications import Starlette
from starlette.requests import Request as request
from starlette.responses import PlainTextResponse
from starlette.endpoints import HTTPEndpoint




class Homepage(StarletteForm):
    name = StringField('name', validators=[DataRequired()])




class User(HTTPEndpoint):
    async def get(self, request):
        username = request.path_params['username']
        return PlainTextResponse(f"Hello, {username}")
