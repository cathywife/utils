#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sys
import os
import urllib2
import cookielib
import urllib
import json


host = ""
auth_username = ""
auth_passwd = ""


class LoginException(Exception):

    '''my defined login exception'''

    def __init__(self, data):
        Exception.__init__(self, data)
        self.__data = data

    def __str__(self):
        return str(self.__data)


class Ldapapi(object):
    is_login = False
    host_url = host

    @classmethod
    def login(cls, username, password, url):
        auth_url = r"http://" + cls.host_url + r"/" + url
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        urllib2.install_opener(opener)
        data = urllib.urlencode({"username": username, 'password': password})
        login_response = urllib2.urlopen(auth_url, data)
        response = login_response.read()

        ret_dict = json.loads(response)

        # update to check the response content to check if passed
        # authentication
        if ret_dict["result"] == "success":
            cls.is_login = True
        else:
            cls.is_login = False

    @classmethod
    def get_wrapper(cls, url, username, password,
                    data_dict, auth_url="api/v1/ldapauth"):
        if not cls.is_login:
            cls.login(username, password, auth_url)

        if not cls.is_login:
            raise LoginException(
                "login to %s failed with username:%s and password:%s"
                % (auth_url, username, password))

        data = urllib.urlencode(data_dict)
        visit_url = r"http://" + cls.host_url + r"/" + url
        login_response = urllib2.urlopen(visit_url + "?" + data)
        response = login_response.read()
        ret_dict = json.loads(response)

        return ret_dict

    @classmethod
    def post_wrapper(cls, url, username, password,
                     data_dict, auth_url="api/v1/ldapauth"):
        if not cls.is_login:
            cls.login(username, password, auth_url)

        if not cls.is_login:
            raise LoginException(
                "login to %s failed with username:%s and password:%s"
                % (auth_url, username, password))

        data = urllib.urlencode(data_dict)
        visit_url = r"http://" + cls.host_url + r"/" + url
        login_response = urllib2.urlopen(visit_url, data)
        response = login_response.read()
        ret_dict = json.loads(response)

        return ret_dict

    @classmethod
    def put_wrapper(cls, url, username, password,
                    data_dict, auth_url="api/v1/ldapauth"):
        if not cls.is_login:
            cls.login(username, password, auth_url)

        if not cls.is_login:
            raise LoginException(
                "login to %s failed with username:%s and password:%s"
                % (auth_url, username, password))

        data = urllib.urlencode(data_dict)
        visit_url = r"http://" + cls.host_url + r"/" + url

        request = urllib2.Request(visit_url, data=data)
        request.get_method = lambda: 'PUT'
        login_response = urllib2._opener.open(request)
        response = login_response.read()
        ret_dict = json.loads(response)

        return ret_dict

    @classmethod
    def delete_wrapper(cls, url, username, password,
                       data_dict, auth_url="api/v1/ldapauth"):
        if not cls.is_login:
            cls.login(username, password, auth_url)

        if not cls.is_login:
            raise LoginException(
                "login to %s failed with username:%s and password:%s"
                % (auth_url, username, password))

        data = urllib.urlencode(data_dict)
        visit_url = r"http://" + cls.host_url + r"/" + url

        request = urllib2.Request(visit_url + "?" + data)
        request.get_method = lambda: 'DELETE'
        login_response = urllib2._opener.open(request)
        response = login_response.read()
        ret_dict = json.loads(response)

        return ret_dict
