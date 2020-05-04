import time
from datetime import datetime
from random import randint

from requests_html import HTMLSession

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


def post_answer(session, url, data):
    '''
    提交答案
    '''
    r = session.post(url, data)
    print('提交返回结果:{}'.format(r.text))


def simulate_survey():
    '''
    模拟回答问卷
    '''

    session = HTMLSession()
    resp = session.get(QUESTION_URL)
    url = parse_post_url(resp)
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
