from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Message, Scope, Receive, Send


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



# class ASGIMiddleware:
#     def __init__(self, app: ASGIApp) -> None:
#         self.app = app

#     async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
#         if scope["type"] != "http":
#             return await self.app(scope, receive, send)

#         async def send_wrapper(message: Message) -> None:
#             # ... Do something
#             await send(message)

#         await self.app(scope, receive, send_wrapper)