import logging
import os.path
import urllib.request
from mimetypes import MimeTypes
from pathlib import Path

from .status import Status
from .response import Response

PUBLIC_PATH = 'public'  # TODO: pass arbitrary path from cli
BAD_REQUEST_HTML = open('%s/400.html' % PUBLIC_PATH, 'rb').read()
FORBIDDEN_HTML = open('%s/403.html' % PUBLIC_PATH, 'rb').read()
NOT_FOUND_HTML = open('%s/404.html' % PUBLIC_PATH, 'rb').read()
HTML_MIME = 'text/html;charset=utf8'

log = logging.getLogger('simple-http-server')
mime = MimeTypes()


def handle_request(request):
    if request is None:
        return Response(Status.BAD_REQUEST, HTML_MIME, BAD_REQUEST_HTML)

    relative_path = request.path[1:]
    resource_path = Path(PUBLIC_PATH).joinpath(relative_path)
    log.debug('resource_path: %s' % resource_path)

    if not os.path.normpath(resource_path).startswith(PUBLIC_PATH):
        return Response(Status.FORBIDDEN, HTML_MIME, FORBIDDEN_HTML)

    if resource_path.is_file():
        url = urllib.request.pathname2url(bytes(resource_path))
        mime_type = mime.guess_type(url)
        body = open(resource_path, 'rb').read()
        return Response(Status.OK, mime_type[0], body)

    if resource_path.is_dir():
        index_html = resource_path.joinpath('index.html')
        if index_html.exists():
            body = open(index_html, 'rb').read()
            return Response(Status.OK, HTML_MIME, body)

    return Response(Status.NOT_FOUND, HTML_MIME, NOT_FOUND_HTML)
