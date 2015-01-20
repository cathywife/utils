#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 一个 http 请求工具.

使用 urllib2 进行 http 请求, 先生成一个对象, 然后进行请求,
 
忽略了 302, 生成对象的时候验证并获取 cookie, 之后通过 cookie
请求.

"""

import urllib2
import cookielib
import urllib

import ujson as json


HOST = ""
AUTH_USERNAME = ""
AUTH_PASSWD = ''
AUTH_API = ''


class HTTPCookieRedirectHandler(urllib2.HTTPRedirectHandler):
    """ 默认 urllib2 遇到 302 会自动跳转, 而且不带 cookie.

    这里把 302 去掉, 不再跳转;

    """
    def http_error_302(self, req, fp, code, msg, headers):
        infourl = urllib.addinfourl(fp, headers, req.get_full_url())
        infourl.status = code
        infourl.code = code
        return infourl

    http_error_300 = http_error_302
    http_error_301 = http_error_302
    http_error_303 = http_error_302
    http_error_307 = http_error_302


class LoginException(Exception):
    def __init__(self, data):
        Exception.__init__(self, data)
        self.__data = data

    def __str__(self):
        return str(self.__data)


class Ldapapi(object):
    def __init__(self, host_url=HOST, username=AUTH_USERNAME, \
            password=AUTH_PASSWD, auth_uri=AUTH_API):
        self.is_login = False
        self.host_url = host_url
        self.username = username
        self.password = password
        self.auth_uri = auth_uri
        self.cookies = None   # 我们把 cookie 保存, 初始化对象的时候生成.

        self.login()
        if not self.is_login:
            raise LoginException("asset auth failed.")

    def login(self):
        opener = urllib2.build_opener(HTTPCookieRedirectHandler)
        urllib2.install_opener(opener)
        urllib2._opener.handlers[1].set_http_debuglevel(100)

        auth_url = r"http://" + self.host_url + r"/" + self.auth_uri
        data_dict = {"j_username": self.username, 'j_password': self.password}
        data = urllib.urlencode(data_dict)   
        request = urllib2.Request(auth_url, data)
        login_response = urllib2._opener.open(request)
        if login_response.code == 302:
            self.is_login = True
            self.cookies = login_response.info()['Set-Cookie']

    def post_wrapper(self, url, data_dict):
        data = urllib.urlencode(data_dict)
        visit_url = r"http://" + self.host_url + r"/" + url

        request = urllib2.Request(visit_url, data)
        request.add_header("Cookie", self.cookies)
        login_response = urllib2.urlopen(request)
        response = login_response.read()
        ret_dict = json.loads(response)

        return ret_dict

    def get_wrapper(self, url, data_dict):
        data = urllib.urlencode(data_dict)
        visit_url = r"http://" + self.host_url + r"/" + url

        request = urllib2.Request(visit_url + "?" + data)
        request.add_header("Cookie", self.cookies)
        login_response = urllib2.urlopen(request)
        response = login_response.read()
        ret_dict = json.loads(response)

        return ret_dict

    def put_wrapper(cls, url, data_dict):
        data = urllib.urlencode(data_dict)
        visit_url = r"http://" + self.host_url + r"/" + url

        request = urllib2.Request(visit_url, data)
        request.get_method = lambda: 'PUT'
        request.add_header("Cookie", self.cookies)
        login_response = urllib2.urlopen(request)
        response = login_response.read()
        ret_dict = json.loads(response)

        return ret_dict

    def delete_wrapper(cls, url, data_dict):
        data = urllib.urlencode(data_dict)
        visit_url = r"http://" + self.host_url + r"/" + url

        request = urllib2.Request(visit_url + "?" + data)
        request.get_method = lambda: 'DELETE'
        request.add_header("Cookie", self.cookies)
        login_response = urllib2.urlopen(request)
        response = login_response.read()
        ret_dict = json.loads(response)

        return ret_dict
