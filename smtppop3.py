#!/usr/bin/env python

from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp.126.com'
POP3SVR = 'pop.sina.com'

origHdrs = ['From: xjr30226@126.com',
            'To: xjr7670@sina.com',
            'Subject: test msg']
origBody = ['xx', 'yy', 'zz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs), '\r\n'.join(origBody)])

sendSvr = SMTP(SMTPSVR)
l = sendSvr.login('xjr30226', 'X45668668')
errs = sendSvr.sendmail('xjr30226@126.com', ('xjr7670@sina.com', ), origMsg)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)

recvSvr = POP3(POP3SVR)
recvSvr.user('xjr7670')
recvSvr.pass_('x45668668')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
# strip headers and compare to orig msg
sep = msg.index('')
recvBody = msg[sep+1:]
assert origBody == recvBody   # assert identical
