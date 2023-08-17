from starlette.applications import Starlette
from starlette_wtf import csrf_protect, form, util
from starlette.requests import Request
from starlette.routing import Route, Mount, Router
from forms import Homepage
from starlette.responses import Response, HTMLResponse, PlainTextResponse
import jinja2
from jinja2 import Template
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from starlette.templating import Jinja2Templates

env = Environment(loader=FileSystemLoader('templates'))
templates = Jinja2Templates(env=env)
request = Request





@csrf_protect
async def homepage(request):
    """GET|POST /: form handler
    """
    form = await Homepage.from_formdata(request)
    template =  'index.html'
    
    if await form.validate_on_submit():
        return templates.TemplateResponse(template)

    html = await Template.render(template,form=form)
    return HTMLResponse(html)
