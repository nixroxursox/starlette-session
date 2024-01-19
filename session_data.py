from aiohttp import web
from asyncio import get_event_loop
import asyncio

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.routing import Route
from starlette_wtf.form import StarletteRequest
from starlette.responses import (
    Response,
    HTMLResponse,
    PlainTextResponse,
    RedirectResponse,
    JSONResponse,
    Response as response,
    Response as StarletteResponse
)

from routes import (
    app_context,
    form_context,
    root_context,
    auth_context,
    session_context
)

from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
import aiomcache

from forms import LoginForm, User, Profile, RegistrationForm
from starlette.types import ASGIApp, Message, Receive, Send
from accounts import UserData as u

from starlette_session import SessionMiddleware
from starlette_session.backends import BackendType


env = Environment(
    loader=FileSystemLoader("templates/", encoding="utf-8"),
    auto_reload=True,
    enable_async=True
)

async def session(request: Request) -> JSONResponse:
    request.session.update({"data": "session_data"})
    return JSONResponse({"session": request.session})


async def clear_session(request: Request):
    request.session.clear()
    return JSONResponse({"session": request.session})


async def view_session(request: Request) -> JSONResponse:
    return JSONResponse({"session": request.session})


# 

async def setup_session(request: StarletteRequest) -> RedirectResponse:
    request.session.update({"data": "session_data"})
    #request.session.update({"x-session_id": session_id})
    async with request.form() as form:
        user = form["username"]
        request.session.update({'username': user})
        client_ip = request.headers.get('x-real-ip')
    #user_sess = user + "-" + client_ip + "-" + str(session_id)
    #request.session.update({"session_id": user_sess })
    request.session.update({"clientIp": client_ip })
    request.session.update({"lifetime": 360 })
    request.session.update({"ttl": 100 })
    request.session.update({"path": request.get("path")})
    #session_data = store.update("session_data",session_id,request.session["path"], request.session["ttl"],request.session["username"])
    return RedirectResponse(url=request.url_for("profile"), status_code=200)



# async def build_response(request: StarletteRequest) -> RedirectResponse:
#     user = request.session("username")
#     userid = user
#     cookie = str(bool(user))
#     session = request.session
#     if not user:
#         user = ""

#     return RedirectResponse(url=request.url_for("build_welcome"), status_code=307)
    #     {   
    #         "request": request,
    #         "cookie": cookie,
    #         "session": session,
    #         "welcome": welcome,
    #         "username": user
    #     }
    # )


# async def build_welcome(request: StarletteRequest) -> HTMLResponse:
#     if request.method == "POST":
#         user = request.session("username")
#         userid = user
#         if user and userid:
#             welcome = f"Welcome back {user}! You are logged in."
#         elif user:
#             welcome = f"Welcome back  {user}! Please log in."
#     elif request.method == 'GET':
#         template = env.get_template("profile.html")
#         html = await template.render_async(username = user, userid = user, title=title)
#         return HTMLResponse(html)


# from fastapi import APIRouter, Request, Response
# from fastapi.responses import HTMLResponse, RedirectResponse
# from fastapi.templating import Jinja2Templates


# users = [
#     # Password is the same as the username, just salted and hashed.
#     # Don't do this in a production application! Use custom passwords.
#     { "userid": 1, "username": "admin", 
#         "password": b'$2b$12$6xEcJ9bCRo3JgNWyn32fwuSoRh1pg8f81jjHpYq6NQ9Y8uDkhWOE6'},
#     { "userid": 2, "username": "test", 
#         "password": b'$2b$12$UZLEFMg9ez.n88Sjpb/ZN.VVlmyPPxHOeL/DE452Si4H3PSQSB0Pa'}
# ]

# router = APIRouter(prefix="/lesson12")
# templates = Jinja2Templates(directory="templates")

# @router.get("/", response_class=HTMLResponse)
# async def get_lesson12(request: Request):
#     username = request.cookies.get("username")
#     userid = request.session.get("userid")
#     return build_response(request, username, userid)

# @router.post("/", response_class=HTMLResponse)
# async def post_lesson12(request: Request, response: Response):
#     username = request.cookies.get("username")
#     userid = request.session.get("userid")

#     form = dict(await request.form())
    
#     if form.get("reload"):
#         return RedirectResponse(request.url)
    
#     if form.get("log-out"):
#         request.session.clear()
#         userid = None
#         return build_response(request, username, userid)
    
#     if form.get("forget-me"):
#         request.session.clear()
#         response = build_response(request, None, None)
#         response.set_cookie("username", "", expires=0)
#         return response
    
#     if form.get("log-in"):
#         username = form.get("username")
#         password = form.get("password")
#         userid = authenticate_user(username, password)
#         if not userid:
#             return RedirectResponse(request.url, status_code=303)

#         request.session["userid"] = userid
#         response = build_response(request, username, userid)
#         response.set_cookie("username", username)
#         return response

#     return build_response(request, username, userid)

# def build_response(request: Request, username, userid):
#     cookie = str(bool(username))
#     session = str(bool(userid))
#     welcome = build_welcome(username, userid)
#     if not username:
#         username = ""

#     return templates.TemplateResponse(
#         "lesson12.html", 
#         {   
#             "request": request,
#             "cookie": cookie,
#             "session": session,
#             "welcome": welcome,
#             "username": username
#         }
#     )

# def build_welcome(username, userid):
#     if username and userid:
#         welcome = f"Welcome back {username}! You are logged in."
#     elif username:
#         welcome = f"Welcome back  {username}! Please log in."
#     else:
#         welcome = "Welcome! Please log in."
#     return welcome

# # def authenticate_user(username, password):
# #     for user in users:
# #         if user["username"] == username:
# #             result = bcrypt.checkpw(password.encode(), user["password"])
# #             if result:
# #                 # should track successful logins
# #                 return user["userid"]
# #             else:
# #                 # Should track failed attempts, lock account, etc.
# #                 return None
# #     return None

# # def generate_hashed_password(password):
# #     # Use this function to generate hashed passwords to save in 
# #     # the users list or a database.
# #     salt = bcrypt.gensalt()
# #     hashed = bcrypt.hashpw(password, salt)
# #     return hashed
