# simple-http-server

Simple HTTP Server written in Python3 asyncio.

This module supports **3.6 or higher** since it uses variable annotations for type hints.

* [PEP 526 Syntax for Variable Annotations](https://www.python.org/dev/peps/pep-0526/)

## How to run server

* Python 3

```bash
$ cd path/to/simple-http-server/python3-simple-http-server
$ python setup.py develop
$ simple-http-server
2017-11-19 16:23:06,465 INFO: start simple http server, 127.0.0.1:8080
```

## How to test

```bash
$ pip install tox
$ tox -e py36
```
