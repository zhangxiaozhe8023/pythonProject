#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:zhangxiaozhe
# 2020/12/10 16:34
import requests
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time


class SendMail(object):
    def __init__(self, email_info):
        self.email_info = email_info
        # 使用SMTP_SSL连接端口为465
        self.smtp = smtplib.SMTP_SSL(self.email_info['server'], self.email_info['port'])
        # 创建两个变量
        self._attachements = []
        self._from = ''

    def login(self):
        # 通过邮箱名和smtp授权码登录到邮箱
        self._from = self.email_info['user']
        self.smtp.login(self.email_info['user'], self.email_info['password'])

    def sendMail(self):
        # 发送邮件，可以实现群发
        msg = MIMEMultipart()
        contents = MIMEText(self.email_info['content'], 'plain', 'utf-8')
        msg['From'] = self.email_info['user']
        msg['To'] = self.email_info['to']
        msg['Subject'] = self.email_info['subject']

        for att in self._attachements:
            # 从列表中提交附件，附件可以有多个
            msg.attach(att)
        msg.attach(contents)
        try:
            self.smtp.sendmail(self._from, self.email_info['to'].split(','), msg.as_string())
            print('邮件发送成功，请注意查收'.center(30, '#'))
            print("%s:success" % nowdate)
        except Exception as e:
            print('Error:', e)
            print("%s:error" % nowdate)

    def close(self):
        # 退出smtp服务
        self.smtp.quit()
        print('logout'.center(30, '#'))


if __name__ == '__main__':

    # dict_post = {
    #     "UserId": "GM20200226174007084930",
    #     "PicUrl": "http://baidu.com/Fi08yCW8wCJOJNmSoKhlqU_byNtz?imageView2/0/format/jpg",
    #     "bmi": "0",
    # }
    #
    # json_post = json.dumps(dict_post)

    #liu_url2 = "http://192.168.1.6:8666/studentR4ecoder/getClassUseRecoder.action"
    listurl =["http://guanchu.tifenpai.com:9097/olsw/#/index","http://guangao.tifenpai.com:9091/olsw/#/index","http://guangao.tifenpai.com:9090/olsw/#/index","http://jiahe.tifenpai.com:9092/olsw/#/index"]
    project = "ols接口故障告警"
    nowdate = (time.strftime("%Y-%m-%d", time.localtime()))

    for i in range(5):
        try:
            detailtime = (time.strftime("%Y-%m-%d %X", time.localtime()))
            # r1 = requests.post(zhongyi_url, timeout=3, data=json_post, headers={"Content-type": "application/json"})
            r1 = requests.get(listurl[i], timeout=3,headers={"Connection": "keep-alive","Content-Type":"text/html"})
            time.sleep(1)
        except Exception as e:
            res = '接口地址:%s ' % listurl[i] + "\n" + '接口故障或者超时报错内容: %s' % e + "\n" + '故障发生时间:%s' % detailtime
            # 邮件登录及内容信息
            email_dict = {
                # 手动填写，确保信息无误
                "user": "980778026@qq.com",
                "to": "193148037@qq.com,kaysa8023@163.com",
                # 多个邮箱以','隔开；
                "server": "smtp.qq.com",
                'port': 465,  # values值必须int类型
                "username": "980778026@qq.com",
                "password": "mmfrcjqfhqhebcfi",
                "subject": "%s-%s" % (project, nowdate),
                "content": '%s' % res

            }
            sendmail = SendMail(email_dict)
            sendmail.login()
            sendmail.sendMail()
            sendmail.close()

        else:
            if r1.status_code != 200:
                res = '接口地址: %s ' % listurl[i] + "\n" + ' ,接口状态为：%s:' % r1.status_code + "\n" + ' ,接口异常时间: %s' % detailtime
                email_dict = {
                    # 手动填写，确保信息无误
                    "user": "980778026@qq.com",
                    "to": "193148037@qq.com,kaysa8023@163.com",
                    # 多个邮箱以','隔开；
                    "server": "smtp.qq.com",
                    'port': 465,  # values值必须int类型
                    "username": "980778026@qq.com",
                    "password": "mmfrcjqfhqhebcfi",
                    "subject": "%s-%s" % (project, nowdate),
                    "content": '%s' % res

                }
                sendmail = SendMail(email_dict)
                sendmail.login()
                sendmail.sendMail()
                sendmail.close()
            else:
                print('接口地址：%s, 接口响应时间: %s' % (listurl[i], r1.elapsed.total_seconds()) + " ,接口状态为：%s ,时间:%s" % (
                r1.status_code, detailtime) + "\n")

