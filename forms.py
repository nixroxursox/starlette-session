from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
from wtforms.form import Form
from wtforms import validators, widgets
from wtforms.fields.simple import TextAreaField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length
from wtforms.widgets import PasswordInput
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from starlette.endpoints import HTTPEndpoint
from starlette.responses import PlainTextResponse
from starlette.types import typing
from wtforms import Form, BooleanField, StringField, PasswordField, validators



class User(HTTPEndpoint):
    async def get(self, request):
        username = request.path_params['username']
        return PlainTextResponse(f"Hello, {username}")


class LoginForm(Form):

    """login form
    """

    username = StringField(
        name='username',
        label='username',
        id='username',
        validators=[
            DataRequired(),
            length(min=4, max=44, message="Please enter your UserId")
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

    pinCode = PasswordField(
        name='pinCode',
        widget=PasswordInput(hide_value=True),
        validators=[
            DataRequired('Please enter a PIN Code')
        ]
    )
    SubmitField = SubmitField(
        name='submit',
        label='submit',
        id="submit"
    )


class CreateAccountForm(Form):
    """Create account form
    """

    username = StringField(
        name='username',
        label='username',
        id='username',
        validators=[
            DataRequired('Please enter a unique userId'),
        ]
    )

    nickName = StringField(
        name='nickName',
        label='nickName',
        id='nickName',
        validators=[
            DataRequired('Please enter a Display Name'),
        ]
    )

    password = PasswordField(
        name='password',
        label='password',
        id='password',

        widget=PasswordInput(hide_value=True),
        validators=[
            DataRequired('Please enter your password')
        ]
    )

    pinCode = PasswordField(
        name='pinCode',
        label='pinCode',
        id='pinCode',

        widget=PasswordInput(hide_value=True),
        validators=[
            DataRequired('Please enter a PIN Code')
        ]
    )

    statement = TextAreaField(
        name='statement',
        label='statement',
        id='statement',
        validators=[
            DataRequired(
                'Please enter a personal Statement to prevent Phishing')
        ]
    )

    pgp = TextAreaField(
        name='pgpKey',
        label='pgpKey',
        id='pgpKey',
        validators=[
            DataRequired(
                'Please enter a personal Statement to prevent Phishing'),
            validators.length(min=150, max=10000,
                              message="Please enter PGP key")
        ]
    )
    SubmitField = SubmitField(
        name='submit',
        label='submit',
        id='submit',
    )


class Profile(HTTPEndpoint):
    """ logged in profile mods for Users """
    async def __init__(self, profileData) -> None:
        pass



class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])