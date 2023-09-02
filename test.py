from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import PlainTextResponse, HTMLResponse, JSONResponse, Response, Response as response
from starlette_wtf import StarletteForm, CSRFProtectMiddleware, csrf_protect
from wtforms import StringField
from wtforms.validators	import DataRequired
from starlette.testclient import TestClient
import typing
from wtforms.form import Form

from starlette.requests import Request as request, Request


async def app_context(request: Request) -> typing.Dict[str, typing.Any]:
    return {'app': request.app}
env = Environment(
    loader=FileSystemLoader("templates/", encoding='UTF-8'),
    auto_reload=True,
    enable_async=True
)




class MyForm(StarletteForm):
    name = StringField('name', validators=[DataRequired()])


template = Template('''
<html>
  <body>
    <form method="post" novalidate>
      {{ form.csrf_token }}
      <div>
        {{ form.name(placeholder='Name') }}
        {% if form.name.errors -%}
        <span>{{ form.name.errors[0] }}</span>
        {%- endif %}
      </div>
      <button type="submit">Submit</button>
    </form>
  </body>
</html>
''')


app = Starlette(middleware=[
    Middleware(SessionMiddleware, secret_key='***REPLACEME1***'),
    Middleware(CSRFProtectMiddleware, csrf_secret='***REPLACEME2***')
])


@app.route('/', methods=['GET', 'POST'])
@csrf_protect
async def index(request):
    """GET|POST /: form handler
    """
    form = await MyForm.from_formdata(request)

    if await form.validate_on_submit():
        return PlainTextResponse('SUCCESS')

    html = template.render(form=form)
    return HTMLResponse(html)





def test_homepage():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert "request" in response.content


class CreateAccountForm(StarletteForm):
    """Create account form
    """
    """registration form
    """

    username = TextAreaField(
        name = 'username',
        label = 'username',
        id = 'username',
        validators=[
            DataRequired('Please enter a unique userId'),
        ]
    )

    nickName = TextAreaField(
        name = 'nickName',
        label = 'nickName',
        id = 'nickName',
        validators=[
            DataRequired('Please enter a Display Name'),
        ]
    )

    password = PasswordField(
        name = 'password',
        label = 'password',
        id = 'password',
        
        widget=PasswordInput(hide_value=True),
        validators=[
            DataRequired('Please enter your password')
        ]
    )

    pinCode = PasswordField(
        name = 'pinCode',
        label = 'pinCode',
        id = 'pinCode',
        
        widget=PasswordInput(hide_value=True),
        validators=[
            DataRequired('Please enter a PIN Code')
        ]
    )
    
    statement = TextAreaField(
        name = 'statement',
        label = 'statement',
        id = 'statement',
        validators=[
            DataRequired('Please enter a personal Statement to prevent Phishing')
        ]
    )

    pgp = TextAreaField(
        name = 'pgpKey',
        label = 'pgpKey',
        id = 'pgpKey',
        validators=[
            DataRequired('Please enter a personal Statement to prevent Phishing'),
            validators.length(min=150, max=10000, message = "Please enter PGP key")
        ]
    )
    SubmitField = SubmitField(
        name = 'submit',
        label='submit',
        id = 'submit',
    )
