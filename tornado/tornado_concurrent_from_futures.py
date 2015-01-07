#-*- coding: utf-8 -*-

"""
    通过 futures 模块实现 tornado 并发.
    需要安装 futures:
        pip install futures

    futures 官方文档:
        https://docs.python.org/3/library/concurrent.futures.html
"""


import tornado.ioloop
import tornado.web

import tornado.web
from tornado import gen

from concurrent.futures import ThreadPoolExecutor


class MainHandler(tornado.web.RequestHandler):
    global executor
    executor = ThreadPoolExecutor(max_workers=3)

    @tornado.gen.coroutine   
    def get(self):
        name = self.get_argument('name', None)
        ret = yield executor.submit(__echo, name)
        self.write(ret)

    def __echo(i):
        return i


application = tornado.web.Application([
    (r"/", MainHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
