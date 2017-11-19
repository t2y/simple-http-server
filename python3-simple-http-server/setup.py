import sys

from setuptools import setup


setup(
    name='simple_http_server',
    version='0.1.0',
    description='Simple HTTP Server',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    url='https://github.com/t2y/simple-http-server',
    license='Apache License 2.0',
    author='Tetsuya Morimoto',
    author_email='tetsuyamorimoto@gmail.com',
    zip_safe=False,
    platforms=['unix', 'linux', 'osx', 'windows'],
    include_package_data=True,
    tests_require=[
        'tox', 'pytest', 'pytest-pep8', 'pytest-flakes',
    ],
    entry_points = {
        'console_scripts': [
            'simple-http-server=simple_http_server.main:main',
        ],
    },
)
