import asyncio
import aiomcache
import datetime
from datetime import datetime
from starlette.applications import Starlette
from starlette.responses import HTMLResponse, RedirectResponse, JSONResponse, PlainTextResponse
from starlette.routing import Route
import uvicorn
import datetime
from asyncio import sleep
from datetime import datetime, tzinfo, timezone
import nacl
from nacl import signing, encoding, utils
from nacl.encoding import URLSafeBase64Encoder
from urllib.parse import quote_plus
from starlette.requests import Request, Request as request
from starlette.responses import Response, JSONResponse
from accounts import UserData as u
from nacl.encoding import Base64Encoder
from nacl.signing import SigningKey
from decouple import config
from starlette_session import AioMemcacheSessionBackend
from starlette_session.backends import BackendType


signKey = config('SIGN_KEY')
verKey = config('VER_KEY')
backend_type = BackendType.aioMemcache
backend_client = aiomcache.Client
host = "dockerswarm-memcached-1"
port = 11211
mc = aiomcache.Client(host, port)
time_and_date = datetime.now()
rand = nacl.utils.random(32)
make_signer = nacl.signing.SigningKey.generate()
signer = nacl.signing.SigningKey(rand)
max_age = 3500


# resp_headers = ({
#     'X-CSRFToken': 'csrf_token',
#     'X-Auth-Token': 'session_token',
#     'Authorization': 'Bearer',
#     'X-Content-Type-Options': 'nosniff',
#     'Referrer': 'http://',
#     'X-XSS-Protection': 'block'
#     }
# )


# sess_date = {}
# sess_data['userId'] = 'userId'
# sess_data['statement'] = 'statement'
# sess_data['csrf_token'] = csrf_token

async def hello_aiomcache():
    mc = aiomcache.Client(host, port)
    await mc.set(b"some_key", b"Some value")
    value = await mc.get(b"some_key")
    values = await mc.multi_get(b"some_key", b"other_key")
    print(values)
    await mc.delete(b"another_key")

asyncio.run(hello_aiomcache())

# async def setup_session(request: Request) -> JSONResponse:
#     mc = aiomcache.Client(host, port)
#     app_data = response.app
#     headers = response.init_headers('resp_headers', response: Response)
#     sess_data = {}
#     sess_data = request.session
    
#     for k, v in sess_data.items():
#         await mc.set(b'k', b'v')
        
    
#     request.session.update({"headers": "session_data"})
#     return JSONResponse({"session": request.session})


# async def clear_session(request: Request):
#     request.session.clear()
#     return JSONResponse({"session": request.session})


# def view_session(request: Request) -> JSONResponse:
#     return JSONResponse({"session": request.session})



# import json
# from typing import Any, Optiona

# import itsdangerous
# from itsdangerous.exc import BadTimeSignature, SignatureExpired
# from starlette.datastructures import MutableHeaders
# from starlette.requests import HTTPConnection
# from starlette.types import ASGIApp, Message, Receive, Scope, Send

# from starlette_session.backends import (AioMemcacheSessionBackend,
#                                         AioRedisSessionBackend, BackendType,
#                                         MemcacheSessionBackend,
#                                         RedisSessionBackend)
# from starlette_session.interfaces import ISessionBackend


# class UnknownPredefinedBackend(Exception):
#     pass

# class Signer:
#     def __init__(self, message):
#         self.message = message


#     def sign(self, message):
#         session_name = nacl.utils.random(8)
#         signer = SigningKey.generate()
#         unsigner = signer.verify_key
#         signed_b64 = signer.sign(message, encoder=URLSafeBase64Encoder)
#         return  signed_b64

#     def unsign(self, signed_b64):
        
#         verify_key = self.sign.unsigner
#         verified = verify_key.verify(signed_b64, encoder=URLSafeBase64Encoder)
#         if verified:
#             return verified
#         return False
        
        
# \
#         connection = HTTPConnection(scope)
#         initial_session_was_empty = True

#         if self.session_name in connection.cookies:
#             try:
#                 data = self.signer.unsign(data, max_age=self.max_age)
#                 if self.backend_type == BackendType.cookie or not self.session_backend:
#                     scope["session"] = json.loads(b64decode(data))
#                 else:
#                     session_key = json.loads(b64decode(data)).get(
#                         self._cookie_session_id_field
#                     )
#                     scope["session"] = await self.session_backend.get(session_key)
#                     scope["__session_key"] = session_key

#                 initial_session_was_empty = False
#             except (BadTimeSignature, SignatureExpired):
#                 scope["session"] = {}
#         else:
#             scope["session"] = {}

#         async def send_wrapper(message: Message, **kwargs) -> None:
#             if message["type"] == "http.response.start":

#                 session_key = scope.pop("__session_key")

#                 if scope["session"]:

#                     if (
#                         self.backend_type == BackendType.cookie
#                         or not self.session_backend
#                     ):
#                         cookie_data = scope["session"]
#                     else:
#                         await self.session_backend.set(
#                             session_key, scope["session"], self.max_age
#                         )
#                         cookie_data = {self._cookie_session_id_field: session_key}

#                     data = b64encode(json.dumps(cookie_data).encode("utf-8"))
#                     data = self.signer.sign(data)

#                     headers = MutableHeaders(scope=message)
#                     header_value = self._construct_cookie(clear=False, data=data)
#                     headers.append("Set-Cookie", header_value)

#                 elif not initial_session_was_empty:

#                     if self.session_backend and self.backend_type != BackendType.cookie:
#                         await self.session_backend.delete(session_key)

#                     headers = MutableHeaders(scope=message)
#                     header_value = self._construct_cookie(clear=True)
#                     headers.append("Set-Cookie", header_value)

#             await send(message)

#         await self.app(scope, receive, send_wrapper)

#     # def _get_predefined_session_backend(
#     #     self, backend_db_client
#     # ) -> Optional[ISessionBackend]:
#     #     if self.backend_type == BackendType.redis:
#     #         return RedisSessionBackend(backend_db_client)
#     #     elif self.backend_type == BackendType.cookie:
#     #         return None
#     #     elif self.backend_type == BackendType.aioRedis:
#     #         return AioRedisSessionBackend(backend_db_client)
#     #     elif self.backend_type == BackendType.memcache:
#     #         return MemcacheSessionBackend(backend_db_client)
#     #     elif self.backend_type == BackendType.aioMemcache:
#     #         return AioMemcacheSessionBackend(backend_db_client)
#     #     else:
#     #         raise UnknownPredefinedBackend()

#     def _construct_session(self, clear: bool = False, data=None) -> str:
#         if clear:
#             u = User
#             if u.is_authenticated is False:
#                 data = f"{self.session_name}=null; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT; Max-Age=0; {self.security_flags}"
#             if u.is_authenticated is True:
#                 salt = u.get_statement("userId")
#                 if salt != False:
#                     sa = nacl.encoding.URLSafeBase64Encoder(salt)
#                     session = f"{self.session_name}={sa}; Path=/; Max-Age={self.max_age}; {self.security_flags}"
#         if self.domain:
#             cookie = f"{session}; Domain={self.domain}"
#         return session


from starlette.applications import Starlette
from starlette.responses import HTMLResponse, RedirectResponse, JSONResponse, PlainTextResponse
from starlette.routing import Route
import uvicorn
import datetime
from asyncio import sleep
