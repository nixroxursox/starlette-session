from wtforms import StringField, SubmitField, PasswordField, TextAreaField, validators, BooleanField, meta, IntegerField
from wtforms.validators import DataRequired,length, ValidationError, InputRequired, Optional, none_of, Length
from wtforms_validators import AlphaNumeric
from wtforms.widgets import PasswordInput, NumberInput
from starlette.endpoints import HTTPEndpoint
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.types import typing, Scope
from starlette.datastructures import MultiDict
from starlette_wtf import form, StarletteForm
from starlette_wtf.form import StarletteRequest
from accounts import UserData as u
from  decouple import config
#from session import setup, get_session
from datetime import datetime, time
from aiohttp import web
from asyncio import get_event_loop
import asyncio
from db.database import dataBase
from accounts import UserData as u
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader


env = Environment(
    loader=FileSystemLoader("templates/", encoding="utf-8"),auto_reload=True, enable_async=True)



class Search(StarletteForm):
    pass


class User(HTTPEndpoint):
    async def get(self, request: StarletteRequest):
        template = env.get_template('index.html')
        return await template.render_async(request=request)



class LoginForm(StarletteForm):
    """ login form """
    username = StringField(
        name='username',
        label='username',
        id = 'username',
        validators=[
            DataRequired(),
            Length(min=4, max=44, message="Please enter your UserId"),
            none_of("\"/\\:#$%\'")
        ]
    )

    password = PasswordField(
        name='password',
        label='password',
        id='password',
        widget=PasswordInput(hide_value=True),
        validators=[
            DataRequired('Please enter your password'),

        ]
    )

    pinCode = StringField(
        name='pinCode',
        label='pinCode',
        id='pinCode',
        validators=[
            DataRequired('Please enter a PIN Code')
        ]
    )
    # SubmitField = SubmitField(
    #     name='submit',
    #     id = 'submit'
    # )


class RegistrationForm(StarletteForm):

    username = StringField(
        name='username',
        label='username',
        id="username",
        validators=[
            InputRequired('Please enter your username'),
            length(min=-1, max=55),
            AlphaNumeric(),
            none_of("\"/\\:#$%\'")
        ]
    )
    
    nname = StringField(
        name='nname',
        label='Display Name',
        id='nname',
        validators=[
            Optional(strip_whitespace=True),
            none_of("\"/\:#$%\'")
        ]
    )

    password = PasswordField(
        name='password',
        label='password',
        id='password',

        widget=PasswordInput(hide_value=True),
        validators=[
            InputRequired(),
            length(min=6, max=55)
        ]
    )

    pinCode = StringField(
        name='pinCode',
        label='pinCode',
        id='pinCode',

        widget=PasswordInput(hide_value=True),
        validators=[
            DataRequired('Please enter a PIN Code'),
            Length(min=4,max=12)
        ]
    )

    statement = StringField(
        name='statement',
        id='statement',
        validators=[
            DataRequired(
                'Please enter a personal Statement to prevent Phishing')
        ]
    )

    pgpKey = TextAreaField(
        name='pgpKey',
        label='PGP Key',
        id='pgpKey',
        validators=[
            DataRequired(
                'Please enter a pgp to help with Identity and Authentication'),
            length(min=150, max=10000,
                              message="Please enter PGP key")
        ]
    )

    async def validate_username(self, field):
        """Asynchronous validator to check if userId is already in-use """
        if await u.py_userid(self, field) is True:
            raise ValidationError('userId is already in use')




class ChangePasswordForm(StarletteForm):
    current_password = PasswordField(validators=[validators.DataRequired()])
    new_password = PasswordField(validators=[validators.DataRequired()])
    confirm_new_password = PasswordField(
        validators=[
            validators.DataRequired(),
            validators.EqualTo("new_password", message="The passwords do not match."),
        ]
    )


class passwordValidator:
    def __init__(self, password) -> None:
        self.password = password

    def __call__(self,password):
        return self.password_quality(password)

    def password_quality(password: str) -> dict:
        """ return quality of password with explanation """
        result: dict = {  # noqa - silence complaint about dict init...
            'short': len(password) < config('PASSWORD_MIN_LEN'),
            # long: not checked -> can a password be too long?
            'only_letters': password.isalnum(),
            'only_lower': password.lower() == password,
            'only_upper': password.upper() == password,
            'only_digits': password.isdigit(),
            'only_symbols': re.search(r"^\W*$", password) is None,
            'no_letters': re.search(r"\w*", password) is None,
            'no_upper': not any([i.isupper() for i in password]),
            'no_lower': not any([i.islower() for i in password]),
            'no_digits': re.search(r"\d", password) is None,
            'no_symbols': re.search(r"\W", password) is None
        }

        result['quality'] = {
            'quality': len(result) - len([i for i in result if i]),
            'max': len(result)
        }
        result['only'] = any([value for key, value in result.items() if 'only_' in key[:5]])
        result['no'] = any([value for key, value in result.items() if 'no_' in key[:3]])
        result['ok'] = not (result['short'] or result['only'] or result['no'])
        result['length'] = len(password)

        return result




# class SessionHandler(HTTPEndpoint):
#     def __init__(self):
#         self.loop = asyncio.get_event_loop()
#         self.max_age: int  = 3600 * 24 * 365 # 1 year
        

#     @staticmethod
#     async def handler(request):
#         session = await get_session(request)
#         last_visit = session['last_visit'] if 'last_visit' in session else None
#         session['last_visit'] = time.time()
#         text = 'Last visited: {}'.format(last_visit)
#         return PlainTextResponse(content=text)


class Profile(StarletteForm):


    username = StringField(
        'username',
        validators=[
            InputRequired('Please enter your username'),
            length(min=-1, max=55),
            AlphaNumeric()
        ]
    ) 
    SubmitField = SubmitField(
        name='submit',
        label='submit',
        id='submit',
    )


class ExtraResponseHeadersMiddleware:
    def __init__(self, app, headers):
        self.app = app
        self.headers: dict = headers

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        async def send_with_extra_headers(message):
            if message["type"] == "http.response.start":
                headers = MutableHeaders(scope=message)
                for key, value in self.headers:
                    headers.append(key, value)

            await send(message)

        await self.app(scope, receive, send_with_extra_headers)