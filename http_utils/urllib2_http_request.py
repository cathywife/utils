#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 一个不需要验证密码的 http 请求工具.

"""

import urllib
import urllib2

import ujson as json


HOST = ""


class HTTPRequstClass(object):
    def __init__(self, host_url=HOST):
        self.host_url = host_url

    def post_wrapper(self, url, data_dict):
        data = urllib.urlencode(data_dict)
        visit_url = r"http://" + self.host_url + r"/" + url

        request = urllib2.Request(visit_url, data)
        login_response = urllib2.urlopen(request)
        response = login_response.read()
        ret_dict = json.loads(response)

        return ret_dict

    def get_wrapper(self, url, data_dict):
        data = urllib.urlencode(data_dict)
        visit_url = r"http://" + self.host_url + r"/" + url

        request = urllib2.Request(visit_url + "?" + data)
        login_response = urllib2.urlopen(request)
        response = login_response.read()
        ret_dict = json.loads(response)

        return ret_dict

    def put_wrapper(self, url, data_dict):
        data = urllib.urlencode(data_dict)
        visit_url = r"http://" + self.host_url + r"/" + url

        request = urllib2.Request(visit_url, data)
        request.get_method = lambda: 'PUT'
        login_response = urllib2.urlopen(request)
        response = login_response.read()
        ret_dict = json.loads(response)

        return ret_dict

    def delete_wrapper(self, url, data_dict):
        data = urllib.urlencode(data_dict)
        visit_url = r"http://" + self.host_url + r"/" + url

        request = urllib2.Request(visit_url + "?" + data)
        request.get_method = lambda: 'DELETE'
        login_response = urllib2.urlopen(request)
        response = login_response.read()
        ret_dict = json.loads(response)

        return ret_dict

    def patch_wrapper(self, url, data_dict):
        data = urllib.urlencode(data_dict)
        visit_url = r"http://" + self.host_url + r"/" + url

        request = urllib2.Request(visit_url + "?" + data)
        request.get_method = lambda: 'PATCH'
        login_response = urllib2.urlopen(request)
        response = login_response.read()
        ret_dict = json.loads(response)

        return ret_dict
