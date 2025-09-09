from fastapi import Request

from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.settings import is_endpoint_enabled

class ClientAccessMiddleware(BaseHTTPMiddleware):
    """
    Check if the current client make access to requested endpoint
    Check header "X-Client-ID"
    Returns 403 if not allowed
    """
    async def dispatch(self, request: Request, call_next):
        # TODO: remove it ---------------------------
        if (
            request.url.path.startswith("/docs")
            or request.url.path.startswith("/redoc")
            or request.url.path.startswith("/openapi.json")
        ):
            response = await call_next(request)
            return response
        #---------------------------------------------------------------------------
        client_id = request.headers.get("X-Client-ID")
        if not client_id:
            return JSONResponse(status_code=400, content={"detail": "Missing X-Client-ID header"})

        method = request.method
        path = request.url.path

        if path.startswith("/articles/") and path.count("/") == 2:
            path = "/articles/{id}"

        if not is_endpoint_enabled(client_id, method, path):
            return JSONResponse(status_code=403, content={"detail": "Endpoint not allowed for this client"})

        response = await call_next(request)
        return response