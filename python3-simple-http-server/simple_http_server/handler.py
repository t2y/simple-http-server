import argparse
import logging
import os.path
import urllib.request
from mimetypes import MimeTypes
from pathlib import Path
from typing import Optional, Tuple

from .request import Request
from .response import Response
from .status import Status

HTML_MIME = 'text/html;charset=utf8'

log = logging.getLogger('simple-http-server')
mime = MimeTypes()


def handle_request(args: argparse.Namespace, request: Request) -> Response:
    if request is None:
        return Response(Status.BAD_REQUEST, HTML_MIME, args.bad_request_html)

    relative_path = request.path[1:]
    resource_path = Path(args.public_path).joinpath(relative_path)
    log.debug('resource_path: %s' % resource_path)

    if not os.path.normpath(str(resource_path)).startswith(args.public_path):
        return Response(Status.FORBIDDEN, HTML_MIME, args.forbidden_html)

    if resource_path.is_file():
        url = urllib.request.pathname2url(str(resource_path))
        mime_type: Tuple[Optional[str], ...] = mime.guess_type(url)
        body = open(resource_path, 'rb').read()
        return Response(Status.OK, mime_type[0], body)

    if resource_path.is_dir():
        index_html = resource_path.joinpath('index.html')
        if index_html.exists():
            body = open(index_html, 'rb').read()
            return Response(Status.OK, HTML_MIME, body)

    return Response(Status.NOT_FOUND, HTML_MIME, args.not_found_html)
