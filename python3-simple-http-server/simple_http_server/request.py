

class Request():

    def __init__(self, method: str, path: str, http_version: str) -> None:
        self.method = method
        self.path = path
        self.http_version = http_version

    def __repr__(self) -> str:
        return '%s Request %s %s' % (self.method, self.path, self.http_version)
