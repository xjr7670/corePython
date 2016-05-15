#!/usr/bin/env python

import urllib2

LOGIN = 'admin'
PASSWD = 'x45668668'
URL = 'http://www.xjr7670.com/index.php/action/login?_=f9e7d732a26f9f04ef0d30540dd397bb'

def handler_version(url):
    from urlparse import urlparse as up
    hdlr = urllib2.HTTPBasicAuthHandler()
    hdlr.add_password('Archives', up(url)[1], LOGIN, PASSWD)
    opener = urllib2.build_opener(hdlr)
    urllib2.install_opener(opener)
    return url

def request_version(url):
    from base64 import encodestring
    req = urllib2.Request(url)
    b64str = encodestring('%s:%s' % (LOGIN, PASSWD))[:-1]
    req.add_header("Authorization", "Basic %s" % b64str)
    return req

for funcType in ('handler', 'request'):
    print '*** Using %s:' % funcType.upper()
    url = eval(funcType+'_version')(URL)
    f = urllib2.urlopen(url)
    print f.readline()
    f.close()
