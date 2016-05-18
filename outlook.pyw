#!/usr/bin/env python

from Tkinter import Tk
from time import sleep
from tkMessageBox import showwarning
import win32com.client as win32

warn = lambda app: showwarning(app, 'Exit?')
RANGE = range(3, 8)

def outlook():
    app = 'Outlook'
    olook = win32.gencache.EnsureDispatch('%s.Application' % app)

    mail = olook.CreateItem(win32.constants.olMailItem)
    recip = mail.Recipients.Add('284182470@qq.com')
    subj = mail.Subject = 'Python-to-%s Demo' % app
    body = ["Line %d" % i for i in RANGE]
    body.insert(0, '%s\r\n' % subj)
    body.append("\r\nTh-th-th-that's all folks!")
    mail.Body = '\r\n'.join(body)
    mail.Send()

    ns = olook.GetNamespace("MAPI")
    obox = ns.GetDefaultFolder(win32.constants.olFolderOutbox)
    obox.Display()

    obox.Item.Item(1).Display()

    warn(app)
    olook.Quit()

if __name__ == '__main__':
    Tk().withdraw()
    outlook()