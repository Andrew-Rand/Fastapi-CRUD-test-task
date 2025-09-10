# Example of client configuration
# Only for demo
#
CLIENT_SETTINGS = {
    "client_a": {
        "version": "v1",
        "enabled_endpoints":
            {
                '/articles': ["POST", "GET"],
                '/articles/{id}': ["GET", "PATCH", "DELETE"],
            }
            # "POST /articles", "GET /articles", "GET /articles/{id}", "PATCH /articles/{id}", "DELETE /articles/{id}"],
    },
    "client_b": {
        "version": "v2",
        "enabled_endpoints":
            {
                '/articles': ["GET"],
                '/articles/{id}': ["GET"],
            },
    },
    "client_c": {},
}

def check_version_allowed(client_id: str, method: str, path: str) -> str | None:
    """
    check if client id is presented in config and return, if given path with given method is allowed
    """
    client = CLIENT_SETTINGS.get(client_id)
    if not client:
        return

    if path in client["enabled_endpoints"] and method in client["enabled_endpoints"][path]:
        return client["version"]


ENDPOINTS_WHITELIST = [
    "/docs",
    "/redoc",
    "/openapi.json",
]
