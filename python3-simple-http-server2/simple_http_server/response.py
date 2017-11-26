from asyncio.streams import StreamWriter
from datetime import datetime
from typing import Optional

from .status import Status


class Response:

    DATE_FORMAT = '%a, %d, %b %Y %H:%M:%S GMT'
    CRLF = '\r\n'

    def __init__(self,
                 status: Status,
                 content_type: Optional[str],
                 body: bytes) -> None:
        self.status = status
        self.content_type = '' if content_type is None else content_type
        self.content_length = len(body)
        self.body = body

    @property
    def header(self) -> str:
        date_str = datetime.strftime(datetime.utcnow(), self.DATE_FORMAT)
        header = (
            "HTTP/1.1 " + self.status.code() + self.CRLF +
            "Date: " + date_str + self.CRLF +
            "Server: Simple Python HTTP Server" + self.CRLF +
            "Content-Type: " + self.content_type + self.CRLF +
            "Content-Length: " + str(self.content_length) + self.CRLF +
            "Connection: Close" + self.CRLF +
            self.CRLF
        )
        return header

    def write_to(self, writer: StreamWriter) -> None:
        writer.write(self.header.encode('utf-8'))
        writer.write(self.body)
