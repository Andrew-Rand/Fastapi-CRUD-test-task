# Example of client configuration
# Only for demo
#
client_settings = {
    # TODO: list of dicts {endpoint: [method, method, method]}
    "client_a": {
        "enabled_endpoints": ["POST /articles", "GET /articles", "GET /articles/{id}", "PATCH /articles/{id}", "DELETE /articles/{id}"],
    },
    "client_b": {
        "enabled_endpoints": ["GET /articles"]
    },
    "client_c": {},
}

def is_endpoint_enabled(client_id: str, method: str, path: str) -> bool:
    key = f"{method.upper()} {path}"
    client = client_settings.get(client_id)
    return client and key in client["enabled_endpoints"]