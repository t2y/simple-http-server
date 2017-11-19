import argparse
import asyncio
import logging

from .protocols import http


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
)
log = logging.getLogger('simple-http-server')


def parse_argument() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.set_defaults(
        host='127.0.0.1',
        port=8080,
        verbose=False,
    )

    parser.add_argument(
        '--host',
        help='set host',
    )
    parser.add_argument(
        '--port',
        help='set port number',
    )

    # for debug
    parser.add_argument(
        '-v', '--verbose', action='store_true',
        help='set verbose mode',
    )

    args = parser.parse_args()
    if args.verbose:
        log.setLevel(logging.DEBUG)

    return args


def main() -> None:
    args = parse_argument()
    log.debug(str(args))

    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(http, args.host, args.port, loop=loop)
    server = loop.run_until_complete(coro)
    log.info('start simple http server, %s:%d' % (args.host, args.port))

    try:
        loop.run_forever()
    except KeyboardInterrupt:  # Serve requests until Ctrl+C is pressed
        pass
    finally:
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()

    log.info('end simple http server')


if __name__ == '__main__':
    main()
