from enum import Enum


class Status(Enum):
    OK = '200 OK'
    BAD_REQUEST = '400 BadRequest'
    FORBIDDEN = '403 Forbidden'
    NOT_FOUND = '404 NotFound'
    INTERNAL_SERVER_ERROR = '500 InternalServerError'

    def code(self):
        return self.value
