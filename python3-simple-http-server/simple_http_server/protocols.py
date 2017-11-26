import argparse
import logging
import os.path
from asyncio.streams import StreamReader, StreamWriter
from typing import Awaitable, Callable, Optional

from .handler import handle_request
from .parser import parse_http

log = logging.getLogger('simple-http-server')


def http(
        args: argparse.Namespace
        ) -> Callable[[StreamReader, StreamWriter], Optional[Awaitable[None]]]:
    args.public_path = os.path.normpath(args.top_dir)
    args.bad_request_html = open('%s/400.html' % args.public_path, 'rb').read()
    args.forbidden_html = open('%s/403.html' % args.public_path, 'rb').read()
    args.not_found_html = open('%s/404.html' % args.public_path, 'rb').read()

    async def async_http(reader: StreamReader, writer: StreamWriter) -> None:
        log.info('start callback')
        request_line: bytes = await reader.readline()
        if not request_line:
            writer.close()

        data = request_line.decode()
        request = await parse_http(data)

        response = handle_request(args, request)
        response.write_to(writer)
        await writer.drain()

        log.info('end callback')
        writer.close()

    return async_http
