import re
from .request import Request

RE_HTTP_PATTERN = re.compile(r'(?P<method>.*) (?P<path>.*?) (?P<version>.*?)')


def parse_http(data: str) -> Request:
    m = re.match(RE_HTTP_PATTERN, data)
    if m is None:
        return None

    d = m.groupdict()
    return Request(d['method'], d['path'], d['version'])
