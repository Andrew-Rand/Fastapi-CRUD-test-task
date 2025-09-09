from fastapi import Request

from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.common.tools import check_id_domain
from app.settings import check_version_allowed, ENDPOINTS_WHITELIST


class ClientAccessMiddleware(BaseHTTPMiddleware):
    """
    Check if the current client make access to requested endpoint
    Check header "X-Client-ID"
    Returns 403 if not allowed
    """
    async def dispatch(self, request: Request, call_next):
        for endpoint in ENDPOINTS_WHITELIST:
            if request.url.path.startswith(endpoint):
                response = await call_next(request)
                return response

        # authorize client
        client_id = request.headers.get("X-Client-ID")
        if not client_id:
            return JSONResponse(status_code=400, content={"detail": "Missing X-Client-ID header"})

        method = request.method
        path = request.url.path

        path = check_id_domain(path)
        api_version = check_version_allowed(client_id, method, path)
        if not api_version:
            return JSONResponse(status_code=403, content={"detail": "Endpoint not allowed for this client"})

        # add required router version to request url
        request.scope["path"] = "/" + api_version + request.scope["path"]
        response = await call_next(request)

        return response