# -*- coding: utf-8 -*-


import tornado.ioloop
import tornado.web


import gevent
from gevent import monkey
# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        """ 请求处理示例代码.

        在这里故意 sleep 1, 注意如果没有上面几行 gevent 
        的代码, 这里的 sleep 1 是阻塞的, 也就是一次只能
        处理一个请求; 
        有了 gevent, 威力大增, 并发量大大提高.

        """
        import time
        time.sleep(1)
        self.write("Hello, world")


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", MainHandler), 
        ]

        tornado.web.Application.__init__(self, handlers)


def get():
    application = Application()
    return application
