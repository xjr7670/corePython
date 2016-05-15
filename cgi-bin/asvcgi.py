#!/usr/bin/env python

from cgi import FieldStorage
from os import environ
from cStringIO import StringIO
from urllib import quote
from urllib import unquote
from string import capwords
from string import strip
from string import split
from string import join

class AdvCGI(object):
    header = 'Content-Type: text/html\n\n'
    url = '/cgi-bin/asvcgi.py'

    formhtml = '''<html><head><title>
        Advanced CGI Demo</title></head>
        <body><h2>Avanced CGI Demo Form</h2>
        <form method="post" action="%s" enctype="multipart/form-data">
        <h3>My Cookie Setting</h3>
        <li><code><b>CPPuser = %s</b></code>
        <h3>Enter cookie value<br />
        <input name="cookie" value="%s"> (<i>optional</i>)</h3>
        <h3>Enter your name<br />
        <input name="person" value="%s"> (<i>required</i>)</h3>
        <h3>What languages can you program in?
        (<i>at least one reqired</i>)</h3>
        %s
        <h3>Enter file to upload</h3>
        <input type="file" name="upfile" value="%s" size=45>
        <p><input type="submit">
        </form></body></html>'''

    langSet = ('Python', 'PERL', 'Java', 'C++', 'PHP', 'C', 'JavaScript')
    langItem = '<input type="checkbox" name="lang" value="%s"%s> %s\n'

    def getCPPCookies(self):        # read cookies from client
        if environ.has_key('HTTP_COOKIE'):
            for eachCookie in map(strip, split(environ['HTTP_COOKIE'], ';')):
                if len(eachCookie) > 6 and eachCookie[:3] == 'CPP':
                    tag = eachCookie[3:7]
                    try:
                        self.cookies[tag] = eval(unquote(eachCookie[8:]))
                    except (NameError, SyntaxError):
                        self.cookies[tag] = unquote(eachCookie[8:])
        else:
            self.cookies['info'] = self.cookies['user'] = ''

        if self.cookies['info'] != '':
            self.who, langStr, self.fn = split(self.cookies['info'], ':')
            self.langs = split(langStr, ',')
        else:
            self.who = self.fn = ''
            self.langs = ['Python']

    def showForm(self):         # show file--out form
        self.getCPPCookies()
        langStr = ''
        for eachLang in AdvCGI.langSet:
            if eachLang in self.langs:
                langStr += AdvCGI.langItem % (eachLang, ' CHECKED', eachLang)
            else:
                langStr += AdvCGI.langItem % (eachLang, '', eachLang)

        if not self.cookies.has_key('user') or self.cookies['user'] == '':
            cookStatus = '<i>(cookie has not been set yet)</i>'
            userCook = ''
        else:
            userCook = cookStatus = self.cookies['user']

        print AdvCGI.header + AdvCGI.formhtml % (AdvCGI.url, cookStatus, userCook, self.who, langStr, self.fn)

    errhtml = '''<html><head><title>
        Advanced CGI Demo</title></head>
        <body><h3>ERROR</h3>
        <b>%s</b><br />
        <form><input type="button" value="back" onclick="window.history.back()"></form>
        </body></html>'''

    def showError(self):
        print AdvCGI.header + AdvCGI.errhtml % (self.error)

    resthtml = '''<html><head><title>
        Advanced CGI Demo</title></head>
        <body><h2>Your Upload Data</h2>
        <h3>Your cookie value is: <b>%s</b></h3>
        <h3>Your name is: <b>%s</b></h3>
        <h3>You can program in the following languages:</h3>
        <ul>%s</ul>
        <h3>Your uploaded file...<br />
        Name: <i>%s</i><br />
        Contents: </h3>
        <pre>%s</pre>
        Click <a href="%s"><b>here</b></a> to return to form.
        </body></html>'''

    def setCPPCookies(self):        # tell client to store cookeis
        for eachCookie in self.cookies.keys():
            print 'Set-Cookie: CPP%s=%s; path=/' % (eachCookie, quote(self.cookies[eachCookie]))

    def doResults(self):        # display results page
        MAXBYTES = 1024
        langlist = ''
        for eachLang in self.langs:
            langlist = langlist + '<li>%s</li>' % eachLang

        filedata = ''
        while len(filedata) < MAXBYTES:     # read file chucks
            data = self.fp.readline()
            if data == '':
                break
            filedata += data
        else:       # truncate if too long
            filedata += '... <b><i>(file truncated due to size)</i></b>'
        self.fp.close()
        if filedata == '':
            filedata = '<b><i>(file upload error or file not given)</i></b>'
        filename = self.fn

        if not self.cookies.has_key('user') or self.cookies['user'] == '':
            cookStatus = '<i>(cookies has not been set yet)</i>'
            userCook = ''
        else:
            userCook = cookStatus = self.cookies['user']

        self.cookies['info'] = join([self.who, join(self.langs, ','), filename], ':')
        self.setCPPCookies()
        print AdvCGI.header + AdvCGI.reshtml % (cookStatus, self.who, langlist, filename, filedata, AdvCGI.url)

    def go(self):       # determine which page to return
        self.cookies = {}
        self.error = ''
        form = FieldStorage()
        if form.keys() == []:
            self.showForm()
            return

        if form.has_key('person'):
            self.who = capwords(strip(form['person'].value))
            if self.who == '':
                self.error = 'Your name is required. (blank)'
        else:
            self.error = 'Your name is required. (missing)'

        if form.has_key('cookie'):
            self.cookie['user'] = unquote(strip(form['cookie'].value))
        else:
            self.cookies['user'] = ''
        
        self.langs = []

        if form.has_key('lang'):
            langdata = form['lang']
            if type(langdata) == type([]):
                for eachLang in langdata:
                    self.langs.append(eachLang.value)
                else:
                    self.langs.append(langdata.value)
            else:
                self.error = 'At least one language required.'

        if form.has_key('upfile'):
            upfile = form["upfile"]
            self.fn = upfile.filename or ''
            if upfile.file:
                self.fp = upfile.file
            else:
                self.fp = StringIO('(no data)')
        else:
            self.fp = StringIO('(no file)')
            self.fn = ''

        if not self.error:
            self.doResults()
        else:
            self.showError()

if __name__ == '__main__':
    page = AdvCGI()
    page.go()
    debug = True
