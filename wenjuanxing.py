import requests
import urllib.request
import re
import time
import random
from fake_useragent import UserAgent
import os
from requests_html import HTMLSession
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class WenJuanXing:
    def __init__(self, url):
        """
        :param url:要填写的问卷的url
        """
        self.wj_url = url
        self.post_url = None
        self.header = None
        self.cookie = None
        self.data = None
        self.location = os.getcwd() + '/fake_useragent.json'
        self.ua = UserAgent(path=self.location)

    def set_data(self):
        """
        这个函数中生成问卷的结果，可根据问卷结果，随机生成答案
        :return:
        """
        session = HTMLSession()
        resp = session.get(self.wj_url)
        questions = resp.html.find('fieldset', first=True).find('.div_question')
        post_data = {'submitdata': ""}

        for i, q in enumerate(questions):
            choices = [t.text for t in q.find('label')]

            questions_type = q.find('a', first=True).attrs['class'][0]
            random_index = 1
            if questions_type == 'jqRadio':
                random_index = random.randint(1, len(choices))
            elif questions_type == 'jqCheckbox':
                random_index = '|'.join(list(map(str, random.sample(range(1, len(choices)+1), random.randint(1, len(choices))))))
            else:
                pass

            post_data['submitdata'] += '{}${}}}'.format(i + 1, random_index)
            time.sleep(0.5)
        # 去除最后一个不合法的`}`
        post_data['submitdata'] = post_data['submitdata'][:-1]
        self.data = post_data

    def get_ip(self):
        headers = {
            'User-Agent': self.ua.random
        }
        html = urllib.request.Request(url='https://www.xicidaili.com/nn/', headers=headers)
        html = urllib.request.urlopen(html).read().decode('utf-8')
        reg = r'<td>(.+?)</td>'
        reg = re.compile(reg)
        pools = re.findall(reg, html)[0:499:5]
        #ip = random.choice(pools)
        return pools

    def set_header(self, ip_pools):
        """
        随机生成ip，设置X-Forwarded-For
        ip需要控制ip段，不然生成的大部分是国外的
        :return:
        """
        self.header = {
            'X-Forwarded-For': random.choice(ip_pools),
            'User-Agent': self.ua.random
        }

    def get_ktimes(self):
        """
        随机生成一个ktimes,ktimes是构造post_url需要的参数，为一个整数
        :return:
        """
        return random.randint(15, 50)

    def get_response(self):
        """
        访问问卷网页，获取网页代码
        :return: get请求返回的response
        """
        response = requests.get(url=self.wj_url, headers=self.header)
        self.cookie = response.cookies
        return response

    def get_jqnonce(self, response):
        """
        通过正则表达式找出jqnonce,jqnonce是构造post_url需要的参数
        :param response: 访问问卷网页，返回的reaponse
        :return: 找到的jqnonce
        """
        jqnonce = re.search(r'.{8}-.{4}-.{4}-.{4}-.{12}', response.text)
        return jqnonce.group()

    def get_rn(self, response):
        """
        通过正则表达式找出rn,rn是构造post_url需要的参数
        :param response: 访问问卷网页，返回的reaponse
        :return: 找到的rn
        """
        rn = re.search(r'\d{9,10}\.\d{8}', response.text)
        return rn.group()

    def get_id(self, response):
        """
        通过正则表达式找出问卷id,问卷是构造post_url需要的参数
        :param response: 访问问卷网页，返回的reaponse
        :return: 找到的问卷id
        """
        id = re.search(r'\d{8}', response.text)
        return id.group()

    def get_jqsign(self, ktimes, jqnonce):
        """
        通过ktimes和jqnonce计算jqsign,jqsign是构造post_url需要的参数
        :param ktimes: ktimes
        :param jqnonce: jqnonce
        :return: 生成的jqsign
        """
        result = []
        b = ktimes % 10
        if b == 0:
            b = 1
        for char in list(jqnonce):
            f = ord(char) ^ b
            result.append(chr(f))
        return ''.join(result)

    def get_start_time(self, response):
        """
        通过正则表达式找出问卷starttime,问卷是构造post_url需要的参数
        :param response: 访问问卷网页，返回的reaponse
        :return: 找到的starttime
        """
        start_time = re.search(r'\d+?/\d+?/\d+?\s\d+?:\d{2}', response.text)
        return start_time.group()

    def set_post_url(self, ip_pools):
        """
        生成post_url
        :return:
        """
        self.set_header(ip_pools)  # 设置请求头，更换ip
        response = self.get_response()  # 访问问卷网页，获取response
        ktimes = self.get_ktimes()  # 获取ktimes
        jqnonce = self.get_jqnonce(response)  # 获取jqnonce
        rn = self.get_rn(response)  # 获取rn
        id = self.get_id(response)  # 获取问卷id
        jqsign = self.get_jqsign(ktimes, jqnonce)  # 生成jqsign
        start_time = self.get_start_time(response)  # 获取starttime
        time_stamp = '{}{}'.format(int(time.time()), random.randint(100, 200))  # 生成一个时间戳，最后三位为随机数
        url = 'https://www.wjx.cn/joinnew/processjq.ashx?submittype=1&curID={}&t={}&starttim' \
              'e={}&ktimes={}&rn={}&jqnonce={}&jqsign={}'.format(id, time_stamp, start_time, ktimes, rn, jqnonce, jqsign)
        self.post_url = url  # 设置url
        print(self.post_url)

    def post_data(self):
        """
        发送数据给服务器
        :return: 服务器返回的结果
        """
        self.set_data()
        response = requests.post(url=self.post_url, data=self.data, headers=self.header, cookies=self.cookie)
        return response

    def run(self, ip_pools):
        """
        填写一次问卷
        :return:
        """
        self.set_post_url(ip_pools)
        result = self.post_data()
        print(result.content.decode())

    def mul_run(self, n):
        """
        填写多次问卷
        :return:
        """
        pools = self.get_ip()
        for i in range(n):
            time.sleep(0.1)
            self.run(pools)
            print('第{}次'.format(i+1))


if __name__ == '__main__':
    w = WenJuanXing('https://www.wjx.cn/jq/75738435.aspx')
    w.mul_run(500)
