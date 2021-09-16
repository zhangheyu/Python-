#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


MAIL_BODY = """
    <html>
    <head>
    <style>
    #rcs_tbl {{
        border-collapse: collapse;
        width: 100%;
    }}
    #rcs_tbl td, #rcs_tbl th {{
        border: 1px solid #ddd;
        padding: 8px;
    }}
    #rcs_tbl tr:nth-child(odd) {{ background-color: #F0F8FF; }}
    #rcs_tbl tr:nth-child(even) {{ background-color: #F2F2F2; }}
    </style>
    </head>
    <body>
        <table id="rcs_tbl">
            <col style="width:18%">
            <col style="width:82%">
            <tr>
                <td>severity</td>
                <td><font color=#{0}>{1}</font></td>
            </tr>
            <tr>
                <td>service</td>
                <td>{2}</td>
            </tr>
            <tr>
                <td>ip</td>
                <td>{3}</td>
            </tr>
            <tr>
                <td>type</td>
                <td>{4}</td>
            </tr>
            <tr>
                <td>time</td>
                <td>{5}</td>
            </tr>
            <tr>
                <td>alarm ID</td>
                <td>{6}</td>
            </tr>
            <tr>
                <td>message</td>
                <td>{7}</td>
            </tr>
        </table>
    </body>
    </html>
"""

COLOR = {
    'NORMAL': '493D26',
    'CLEAR': '520D017',
    'INFO': '438D80',
    'WARNING': 'E9AB17',
    'CRITICAL': 'FF0000',
}


class SendMail(object):
    def __init__(self, smtp_server, smtp_port, user, password=None, ssl=False, tls=False):
        self._smtp_server = smtp_server
        self._smtp_port = smtp_port or 25
        self._user = user
        self._password = password
        self._ssl = ssl
        self._tls = tls

    def send(self, to, message):
        msg = MIMEText(message, 'html', 'utf-8')
        msg['Subject'] = 'rcs alarm'
        msg['From'] = formataddr(['rcs admin', self._user])
        msg['To'] = ','.join(to)

        try:
            if self._tls:
                s = smtplib.SMTP(self._smtp_server, self._smtp_port)
                s.set_debuglevel(1)
                s.starttls()
            elif self._ssl:
                s = smtplib.SMTP_SSL(self._smtp_server, self._smtp_port)
            else:
                s = smtplib.SMTP(self._smtp_server, self._smtp_port)

            if self._password is not None:
                s.login(self._user, self._password)
            else:
                s.login(self._user)
            s.set_debuglevel(1)
            s.sendmail(self._user, to, msg.as_string())
            s.quit()
            print('send mail to {} success'.format(to))
        except Exception as e:
            print('send mail to {} failure: {!r}'.format(to, e))
            return False
        return True


def send_mail(mail_conf, to, msg):
    to = to.split(',') if ',' in to else [to]
    sm = SendMail(mail_conf['server'], mail_conf['port'], mail_conf['user'],
                  mail_conf['password'], mail_conf['ssl'], mail_conf['tls'])
    message = MAIL_BODY.format(COLOR[msg['severity']], msg['severity'], msg['service'], msg['ip'],
                               msg['type'], msg['time'], msg['message_id'], msg['message'])
    sm.send(to, message)


# 第三方 SMTP 服务
smtp_host = "smtp.189.cn"  # 设置服务器
smtp_port = 465
mail_user = "abner_zhang@189.cn"  # 用户名
mail_pass = "261219zhy"  # 口令
imap_host = 'imap.189.cn'
imap_port = 993
sender = '18909423767@189.cnn'
receivers = ['heyu.zhang@riversecurity.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


if __name__ == '__main__':
    mc = {
        'server': smtp_host,
        'port': 25,
        'user': mail_user,
        'password': mail_pass,
        'ssl': True,
        'tls': True
    }

    msg_info = {
        'severity': 'NORMAL',
        'service': 'service name',
        'ip': '10.1.1.2',
        'type': 'cpu',
        'time': '2017-03-07 15:11:30',
        'message_id': '348e4380-02e2-11e7-8f22-00e04c682469',
        'message': 'The cpu current usage is 70%, greater than threshold 60%'
    }
    send_mail(mc, 'heyu.zhang@riversecurity.com, 502152574@qq.com', msg_info)
