import time
from datetime import datetime
from random import (randint, choice)
import urllib.request
import requests
import re
from requests_html import HTMLSession
from fake_useragent import UserAgent

from configs import (QUESTION_ID, QUESTION_URL, POST_URL_MAP, ANSWER_TIMES)

from question import (radio, checkBox)


def parse_post_url(resp):
    '''
    解析出提交问卷的url
    '''
    # 找到rn
    rn = int(resp.html.search('rndnum="{}"')[0].split('.')[0])
    # 提交问卷的时间
    raw_t = round(time.time(), 3)
    t = int(str(raw_t).replace('.', ''))
    # 模拟开始答题时间
    starttime = datetime.fromtimestamp(
        int(raw_t) - randint(1, 60 * 3)).strftime("%Y/%m/%d %H:%M:%S")

    url = POST_URL_MAP.format(QUESTION_ID, t, starttime, rn)
    return url


def parse_post_data(resp):
    '''
    解析出问题和选项
    返回post_data
    '''
    post_data = {'submitdata': ""}
    questions = resp.html.find('fieldset', first=True).find('.div_question')

    for i, q in enumerate(questions):
        title = q.find('.div_title_question_all', first=True).text
        print('题目:{}'.format(title))
        
        answer = ''
        question_class = q.find('a', first=True).attrs['class'][0]
        if question_class == 'jqRadio':
            answer = radio(q)
        elif question_class == 'jqCheckbox':
            answer = checkBox(q)
            
        post_data['submitdata'] += '{}${}}}'.format(i+1, answer)
        time.sleep(0.5)

    # 去除最后一个不合法的`}`
    post_data['submitdata'] = post_data['submitdata'][:-1]
    print(post_data)

    return post_data


def get_ip():
    headers = {
        'User-Agent': UserAgent().random
    }
    html = urllib.request.Request(url='https://www.xicidaili.com/nn/', headers = headers)
    html = urllib.request.urlopen(html).read().decode('utf-8')
    reg = r'<td>(.+?)</td>'
    reg = re.compile(reg)
    pools = re.findall(reg, html)[0:499:5]
    Random_IP = choice(pools)
    return Random_IP


def get_headers(User_Agent, Virtual_ip):
    headers = {  # 如果一直不成功可以重新抓包更换一下coookie
        'Host': 'www.wjx.cn',
        'User-Agent': User_Agent,  # 随机浏览器标识
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://www.wjx.cn/jq/'+str(QUESTION_ID)+'.aspx',
        'Cookie': 'acw_tc=2f624a2715707742490114846e11af314ae7a232ed18707c9ed7d7796002c8; .ASPXANONYMOUS=aD0md4y21QEkAAAANmIzNGIzNDEtNDk4OS00MjNjLTg5YTItMjU2YWIwMTdkZGM4_qytsxBWi11-sOz1HwVnB_Y516Q1; jac47027148=19962282; %26ntime%3D1570771906; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1570774251; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1570774251; jpckey=%u5927%u5B66%u751F',  # 这里的cookie，自己提交一遍再抓包，提取出cookie
        'X-Forwarded-For': Virtual_ip  # 随机获取的ip
    }
    return headers


def post_answer(session, url, data):
    '''
    提交答案
    '''
    User_Agent = UserAgent().random  # 随机生成User-Agent
    Virtual_ip = get_ip()
    headers = get_headers(User_Agent, Virtual_ip)
    r = requests.Request('POST', url, data=data)
    prepared = r.prepare()
    print('prepared{}'.format(prepared.__dict__))
    s = requests.Session()
    resp = s.send(prepared, verify=False)
    print('提交返回结果:{}'.format(resp.text))


def simulate_survey():
    '''
    模拟回答问卷
    '''

    session = HTMLSession()
    resp = session.get(QUESTION_URL)
    url = parse_post_url(resp)
    print(url)
    return
    data = parse_post_data(resp)
    post_answer(session, url, data)


def main():
    print('开始模拟填写问卷,共模拟{}次'.format(ANSWER_TIMES))
    for i in range(ANSWER_TIMES):
        simulate_survey()
        sleep_time = randint(1, 60)
        print('第{}次问卷填写完毕，即将沉睡{}s'.format(i+1, sleep_time))
        time.sleep(sleep_time)


if __name__ == '__main__':
    main()
