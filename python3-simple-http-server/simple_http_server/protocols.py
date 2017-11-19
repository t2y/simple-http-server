from asyncio.streams import StreamReader, StreamWriter

from .handler import handle_request
from .parser import parse_http


async def http(reader: StreamReader, writer: StreamWriter) -> None:
    request_line: bytes = await reader.readline()
    if not request_line:
        writer.close()

    data = request_line.decode()
    request = await parse_http(data)

    response = handle_request(request)
    response.write_to(writer)
    await writer.drain()

    writer.close()
