from asyncio.streams import StreamReader, StreamWriter

from .handler import handle_request
from .parser import parse_http
from .request import Request
from .response import Response


async def http(reader: StreamReader, writer: StreamWriter) -> None:
    request_line: bytes = await reader.readline()
    if request_line is None:
        writer.close()

    data: str = request_line.decode()
    request: Request = await parse_http(data)

    response: Response = handle_request(request)
    response.write_to(writer)
    await writer.drain()

    writer.close()
