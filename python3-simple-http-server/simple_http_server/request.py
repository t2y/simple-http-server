

class Request():

    def __init__(self, method, path, http_version):
        self.method = method
        self.path = path
        self.http_version = http_version

    def __repr__(self):
        return '%s Request %s %s' % (self.method, self.path, self.http_version)
