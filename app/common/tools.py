def check_id_domain(path: str) -> str:
    """
    If the last domain of path is id, like 'articles/36, change it to fastAPI pattern {id}
    If not - returns path without changing
    '"""
    domains = path.split("/")
    try:
        int(domains[-1])
        domains[-1] = "{id}"
        path = '/'.join(domains)
    except ValueError:
        pass
    return path