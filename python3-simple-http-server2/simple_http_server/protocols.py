import argparse
import asyncio
import logging
import os.path
from typing import Any

from .handler import handle_request
from .parser import parse_http

log = logging.getLogger('simple-http-server')


def http(args: argparse.Namespace) -> Any:  # FIXME: forward reference?
    args.public_path = os.path.normpath(args.top_dir)
    args.bad_request_html = open('%s/400.html' % args.public_path, 'rb').read()
    args.forbidden_html = open('%s/403.html' % args.public_path, 'rb').read()
    args.not_found_html = open('%s/404.html' % args.public_path, 'rb').read()

    class AsyncHTTP(asyncio.Protocol):

        def connection_made(self, transport: Any) -> None:
            peername = transport.get_extra_info('peername')
            if peername is None:
                return

            log.info('Connection from %s:%d' % peername)
            self.transport = transport

        def data_received(self, data: bytes) -> None:
            message = data.decode()
            request = parse_http(message)

            response = handle_request(args, request)
            response.write_to(self.transport)

            log.info('Close the client socket')
            self.transport.close()

    return AsyncHTTP
