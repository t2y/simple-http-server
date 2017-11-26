# simple-http-server

Simple HTTP Server written in Python3 asyncio.

This module supports **3.6 or higher** since it uses variable annotations for type hints.

* [PEP 526 Syntax for Variable Annotations](https://www.python.org/dev/peps/pep-0526/)

## How to run server

* Python 3

```bash
$ cd path/to/simple-http-server/python3-simple-http-server
$ python setup.py develop
$ simple-http-server --top-dir ../python3-simple-http-server/public/ --verbose
2017-11-26 12:48:00,727 DEBUG: Namespace(host='127.0.0.1', port=8080, top_dir='../python3-simple-http-server/public/', verbose=True)
2017-11-26 12:48:00,728 INFO: start simple http server, 127.0.0.1:8080
2017-11-26 12:48:24,835 INFO: Connection from 127.0.0.1:51247
2017-11-26 12:48:24,836 DEBUG: resource_path: ../python3-simple-http-server/public/index.html
2017-11-26 12:48:24,837 INFO: Close the client socket
2017-11-26 12:48:24,846 INFO: Connection from 127.0.0.1:51248
2017-11-26 12:48:24,847 DEBUG: resource_path: ../python3-simple-http-server/public/cat.jpg
2017-11-26 12:48:24,847 INFO: Close the client socket
```

## How to test

```bash
$ pip install tox
$ tox -e py36
```
