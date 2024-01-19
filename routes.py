import typing
import jinja2
from jinja2.runtime import Context
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
import datetime
from datetime import datetime
from decouple import config
from wtforms.fields import Field
from wtforms import validators, widgets
from starlette.authentication import requires
from starlette.exceptions import HTTPException
from starlette.datastructures import Headers, MutableHeaders, MultiDict
from starlette.requests import Request, HTTPConnection, Scope
from starlette_wtf import StarletteForm
from starlette_wtf.form import StarletteRequest
from starlette.routing import Router
from webob.cookies import JSONSerializer

# from starsessions import generate_session_id

# from starlette.requests.Request import url_for
from starlette.responses import (
    Response,
    HTMLResponse,
    PlainTextResponse,
    RedirectResponse,
    JSONResponse,
    Response as response,
    Response as StarletteResponse,
)
from forms import LoginForm, User, Profile, RegistrationForm, ChangePasswordForm
from starlette.types import ASGIApp, Message, Receive, Send
from accounts import UserData as u


async def app_context(request: StarletteRequest) -> typing.Dict[str, typing.Any]:
    return await {"app": request.app}


async def form_context(request: StarletteRequest) -> typing.Dict[str, typing.Any]:
    return await {"form": request.form}


async def session_context(request: StarletteRequest) -> typing.Dict[str, typing.Any]:
    return await {"session": request.session}


async def auth_context(request: StarletteRequest) -> typing.Dict[str, typing.Any]:
    return await {"auth": request.user}


async def root_context(request: StarletteRequest) -> typing.Dict[str, typing.Any]:
    return await {"root": StarletteRequest}


env = Environment(
    loader=FileSystemLoader("templates/", encoding="utf-8"),
    auto_reload=True,
    enable_async=True,
)

secret = config("SESS_SECRET_KEY")


#@requires("Authentication")
async def profile(request: StarletteRequest) -> HTMLResponse:
    if request.method == "GET":
        template = env.get_template("profile.html")
        title = "profile"
        session = request.session
        html = await template.render_async(session=session, title=title)
        return HTMLResponse(html)


async def index(request: StarletteRequest) -> HTMLResponse:
    template = env.get_template("index.html")
    tcon = Context.get_all
    html = await template.render_async(request=request, response=response, tcon=tcon)
    return HTMLResponse(html)


# auth_header = request.headers.append('Authorization ' + ":"  + ' Bearer' + csrf_protect)
# app.add_route('/login', login, methods=['GET', 'POST'], name='login')
async def login(request: StarletteRequest) -> Response:
    form = await LoginForm.from_formdata(request)
    if request.method == "POST":
        await form.validate_on_submit()
        user = form.username.data
        pw = form.password.data
        pinCode = form.pinCode.data
        if u.py_userid(user) is True:
            if u.py_v_Pass(user, pw) is True:
                if u.py_v_Pin(user, pinCode) is True:
                    return RedirectResponse(
                        url=request.url_for("setup_session"), status_code=307
                    )
    if request.method == "GET":
        title = "Login"
        url = "/login"
        template = env.get_template("auth/login.html")
        html = await template.render_async(form=form, url=url, title=title)
        return HTMLResponse(html)


async def logout(request: StarletteRequest) -> RedirectResponse:
    request.session.pop("user", None)
    return RedirectResponse("/", status_code=200)



async def register(request: StarletteRequest) -> Response:
    form = await RegistrationForm.from_formdata(request)
    if request.method == "POST":
        valid = await form.validate_on_submit()
        if valid is True:
            try:
                r = u.py_createUser(
                    form.username.data,
                    form.password.data,
                    form.pinCode.data,
                    form.nname.data,
                    form.statement.data,
                    form.pgpKey.data,
                )
                if r is True:
                    return RedirectResponse("/login", status_code=303)
            except HTTPException:
                context = HTTPException
                return RedirectResponse("/register", status_code=307), context
    if request.method == "GET":
        title = "Register"
        url = "/register"
        context = {root_context, form_context, app_context, session_context}
        template = env.get_template("auth/register.html")
        html = await template.render_async(
            context=context, form=form, url=url, title=title
        )
        return HTMLResponse(html)


async def changepass(request: StarletteRequest) -> Response:
    form = await ChangePasswordForm.from_formdata(request)
    if request.method == "POST":
        await form.validate_on_submit()
        current_password = form.password.current_password
        new_password = form.new_password.data
        verify_new_password = form.verify_new_password.data
        if u.py_userid(user) is True:
            if u.py_v_Pass(user, pw) is True:
                return RedirectResponse(
                    url=request.url_for("setup_session"), status_code=307
                )
    if request.method == "GET":
        title = "changepass"
        url = "/changepass"
        template = env.get_template("auth/changepass.html")
        html = await template.render_async(form=form, url=url, title=title)
        return HTMLResponse(html)

# async def setup_session(request: StarletteRequest) -> RedirectResponse:
#     request.session.update({"data": "session_data"})
#     #request.session.update({"x-session_id": session_id})
#     async with request.form() as form:
#         user = form["username"]
#         request.session.update({'username': user})
#         client_ip = request.headers.get('x-real-ip')
#     #user_sess = user + "-" + client_ip + "-" + str(session_id)
#     #request.session.update({"session_id": user_sess })
#     request.session.update({"lifetime": 360 })
#     request.session.update({"ttl": 100 })
#     request.session.update({"path": request.get("path")})
#     #session_data = store.update("session_data",session_id,request.session["path"], request.session["ttl"],request.session["username"])
#     return RedirectResponse(url=request.url_for("profile"), status_code=200)


async def clean(request: StarletteRequest) -> RedirectResponse:
    """Access this view (GET "/clean") to remove all session contents."""
    request.session.clear()
    return RedirectResponse("/")


async def check(request):
    """
    Check if we are in session.
    """
    content = """
        <html>
        <title>starlette authlib demo</title>
        <body>
            your status is: %(status)s, click here to <a href="/%(action)s">%(action)s</a>
        </body></html>
    """
    if not request.session["username"]:
        return Response(
            content % {"status": "logged out", "action": "login"},
            headers={"content-type": "text/html"},
            status_code=401,
        )

    return Response(content % {"status": "logged in", "action": "logout"})


# def view_session(request: Request) -> JSONResponse:
#     return JSONResponse({"session": request.session})


# def update_session(request: Request) -> JSONResponse:
#     return JSONResponse({"session": request.session})


# async def app(scope, receive, send):
#     assert scope['type'] == 'http'
#     request = Request(scope, receive)
#     content = '%s %s' % (request.headers, request.session)
#     response = Response(content, media_type='text/plain')
#     await response(scope, receive, send)

# app.add_route('/', index, methods=['GET'], name='index')
# async def index(request) -> None:
#     form = await HelloForm.from_formdata(request)
#     if request.method == 'POST':
#         form.validate_on_submit()
#         return RedirectResponse('/profile', status_code=307)
#     # title = "The Ring"
#     template = env.get_template('index.html')
#     title = "index"
#     return await template.render_async(form=form, title=title)
# return PlainTextResponse("hello world")
#     # u = User
#     # if u.is_authenticated:
#     #     template = env.get_template('index.html')
#     #     return  await template.render_async(request)
#     return RedirectResponse('/login', status_code=307)
# # async def create_account(request):
#     """GET|POST /create-account: create account form handler
#     """
#     # initialize form
#     form = await CreateAccountForm.from_formdata(request)

#     # validate form
#     if request.method == 'POST':
#         if await form.validate_on_submit():


#             # u = User
#             # data = {}
#             # data["user"] = await form["username"]
#             # data["nname"] = await form["nickName"]
#             # data["pw"] = await form["password"]
#             # data["pi"] = await form["pinCode"]
#             # data["st"] = await form["statement"]
#             # data["pgp"] = await form["pgpKey"]
#             #user = data["user"]
#             # check_user_id = u.v_UserId(u, user)
#             # if check_user_id is False:
#             #     create = u.createUser(u, data.values())
#             #     content = create["content"]
#             #     if create["create"] is True:
#             #         return RedirectResponse(url='/', status_code=303)
#             context = {'request': request, 'form': form}
#             status_code = 422 if form.errors else 200
#             return templates.TemplateResponse('auth/register.html',
#                                       context=context,
#                                       status_code=status_code)


# async def create_account(request):
#     """GET|POST /create-account: create account form handler"""
#     # initialize form
#     async with request.form() as formdata:
#         form = CreateAccountForm(formdata)
#         if request.method == 'POST' and form.validate():
#             user = await form.username.data
#             pw = await form.password.data
#             pin = await form.pinCode.data
#             nname = await form.nickName.data
#             st = await form.statement.data
#             pgp = await form.pgpKey.data
#             u = User
#             u.createUser(u, user, pw, pin, nname, st, pgp)
#         # TODO: Save account credentials before returning redirect response
#             return RedirectResponse(url="/profile", status_code=303)
#         if request.method == 'GET':
#             template = env.get_template("auth/register.html")
#             return await template.render_async(formdata)

#     # return form html
#     # context = {"request": request, "form": form}
#     # status_code = 422 if form.errors else 200

#     # return templates.TemplateResponse("auth/register.html", context=context, status_code=status_code)


# ~@app.route('/register', methods=['GET', 'POST'])
# async def register(request):
#     data = {
#         'username' 'StringField',
#         'email', 'StringField',
#         'password' 'PasswordField',
#         'confirm' 'accept_tos'
#     }
#     async with request.form() as formdata:
#         form = RegistrationForm(request)
#         if request.method == 'POST' and form.validate():
#             user = User(form.username.data, form.email.data,
#             form.password.data)
# #db_session.add(user)
# #flash('Thanks for registering')
#             return RedirectResponse('/login', status_code=307)
#         if request.method == 'GET':
#             template = env.get_template('register.html')
#             return await template.render_async(form=form, data=data)
