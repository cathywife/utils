#!/usr/bin/python
# -*- coding: utf-8 -*-


import gevent
import tornado.wsgi
from gevent import pywsgi

import app


ADDRESS = "127.0.0.1"
PORT = 8080


def main():
    """ 这里用 gevent 的 wsgi 来跑 tornado 写的 application.

    """
    application = app.get()
    wsgi_app = tornado.wsgi.WSGIAdapter(application)

    server = pywsgi.WSGIServer(
        (ADDRESS, PORT), wsgi_app
    )
    server.serve_forever()


if __name__ == '__main__':
    main()
