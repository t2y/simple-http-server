# simple-http-server

Simple HTTP Server written in Python3 asyncio.

This module supports **3.6 or higher** since it uses variable annotations for type hints.

* [PEP 526 Syntax for Variable Annotations](https://www.python.org/dev/peps/pep-0526/)

## How to run server

* Python 3

```bash
$ cd path/to/simple-http-server/python3-simple-http-server
$ python setup.py develop
$ simple-http-server --top-dir ./public/
2017-11-26 14:23:54,180 INFO: start simple http server, 127.0.0.1:8080
2017-11-26 14:23:56,514 INFO: start callback
2017-11-26 14:23:56,515 INFO: end callback
2017-11-26 14:23:56,525 INFO: start callback
2017-11-26 14:23:56,525 INFO: end callback
```

## How to test

```bash
$ pip install tox
$ tox -e py36
```
