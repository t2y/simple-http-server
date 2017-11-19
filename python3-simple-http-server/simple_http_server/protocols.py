from .parser import parse_http
from .handler import handle_request


async def http(reader, writer):
    request_line = await reader.readline()
    if request_line is None:
        writer.close()

    data = request_line.decode()
    request = await parse_http(data)

    response = handle_request(request)
    response.write_to(writer)
    await writer.drain()

    writer.close()
