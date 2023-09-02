import typing
import jinja2
from  jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from wtforms.form import Form
from wtforms.fields import Field
from wtforms import validators, widgets
from starlette.exceptions import HTTPException
from starlette.requests import Request, Request as StarletteRequest, Request as request
from starlette.responses import Response, HTMLResponse, PlainTextResponse, RedirectResponse, JSONResponse
from forms import LoginForm, CreateAccountForm, User, Profile
from starlette.types import ASGIApp, Message, Receive, Scope, Send
from accounts import User


form = Form
async def app_context(request: Request) -> typing.Dict[str, typing.Any]:
    return await {'app': request.app}
async def forms_context(request: Request) -> typing.Dict[str, typing.Any]:
    return await {'form': request.form}
async def session_context(request: Request) -> typing.Dict[str, typing.Any]:
    return await {'session': request.session}
env = Environment(
    loader=FileSystemLoader("templates/", encoding="utf-8"),auto_reload=True, enable_async=True)


# async def profile(request):
#     form = await Profile.from_formdata(request)
#     if request.method == 'GET':
#         context = {"request": request, "form": form}
#         return templates.TemplateResponse("/homepage.html",context=context)

#     if request.method == 'POST':
#         if await form.validate_on_submit():
#             name = form.data["name"]
#             context = {"request": request, "form": form}
#             status_code = 422 if form.errors else 200
#             return templates.TemplateResponse("/create-account.html", context=cot, status_code=status_code)


#auth_header = request.headers.append('Authorization ' + ":"  + ' Bearer' + csrf_protect)
#app.add_route('/login', login, methods=['GET', 'POST'], name='login')
async def login(request):
    form = LoginForm(request.form)
    context = {"request": request, "form": form}
    if request.method == 'POST' and form.validate():
        user = await form.username.data
        password = await form.password.data
        pinCode = await form.pinCode.data
        template = env.get_template('auth/login.html')
        return template.render(form=form)
    
    
    if request.method == 'GET':
        status_code = 422 if form.errors else 200
        template = env.get_template('auth/login.html')
        return template
        
    
# async def app(scope, receive, send):
#     assert scope['type'] == 'http'
#     request = Request(scope, receive)
#     content = '%s %s' % (request.headers, request.session)
#     response = Response(content, media_type='text/plain')
#     await response(scope, receive, send)

async def title(request):
    title = request.url['path']
    return title

#app.add_route('/', index, methods=['GET'], name='index')
async def index(request) -> None:
    if request.session:
        content = await '%s %s' % (request.url.path, request.method)
        template = env.get_template('index.html')
        return  template.render(request, content)
    return RedirectResponse('/login', status_code=307)
# async def create_account(request):
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


async def create_account(request):
    """GET|POST /create-account: create account form handler"""
    # initialize form
    form = await CreateAccountForm(request)
    if request.method == 'POST' and form.validate():
            user = await form.username.data
            pw = await form.password.data
            pin = await form.pinCode.data
            nname = await form.nickName.data
            st = await form.statement.data
            pgp = await form.pgpKey.data
            u = User
            u.createUser(u, user, pw, pin, nname, st, pgp)
        # TODO: Save account credentials before returning redirect response
            return RedirectResponse(url="/profile", status_code=303)
    if request.method == 'GET':
        template = env.get_template("auth/register.html").render(form=form)
        return template

    # return form html
    # context = {"request": request, "form": form}
    # status_code = 422 if form.errors else 200

    # return templates.TemplateResponse("auth/register.html", context=context, status_code=status_code)


async def setup_session(request: Request) -> JSONResponse:
    request.session.update({"data": "session_data"})
    return JSONResponse({"session": request.session})


async def clear_session(request: Request):
    request.session.clear()
    return JSONResponse({"session": request.session})


async def view_session(request: Request) -> JSONResponse:
    return JSONResponse({"session": request.session})



#~@app.route('/register', methods=['GET', 'POST'])
async def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)