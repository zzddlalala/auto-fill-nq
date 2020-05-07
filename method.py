import random
from requests_html import HTMLSession
from random import randint
from init import (WJX_URL, QUESTION_TYPE, SELECTION_COUNT, SELECTION_PORBABILITY)

def probability_index(rate):
    start = 0
    index = 0
    randnum = randint(1, sum(rate))
    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break
    return index

def random_data():
    """
            这个函数中生成问卷的结果，可根据问卷结果，随机生成答案
            :return:
            """
    session = HTMLSession()
    resp = session.get(WJX_URL)
    questions = resp.html.find('fieldset', first=True).find('.div_question')
    post_data = {'submitdata': ""}

    for i, q in enumerate(questions):
        choices = [t.text for t in q.find('label')]

        questions_type = q.find('a', first=True).attrs['class'][0]
        random_index = 1
        if questions_type == 'jqRadio':
            random_index = randint(1, len(choices))
        elif questions_type == 'jqCheckbox':
            random_index = '|'.join(list(map(str, random.sample(range(1, len(choices) + 1), randint(1, len(choices))))))
        else:
            pass

        post_data['submitdata'] += '{}${}}}'.format(i + 1, random_index)
    # 去除最后一个不合法的`}`
    post_data['submitdata'] = post_data['submitdata'][:-1]
    return post_data

def probability_data():
    post_data = {'submitdata': ""}
    if len(QUESTION_TYPE) != len(SELECTION_COUNT) or len(SELECTION_PORBABILITY) != len(SELECTION_COUNT):
        print('数据填写有误，请检查后重新填写')
        exit()
    for i in range(len(QUESTION_TYPE)):
        #单选
        index = 1
        if QUESTION_TYPE[i] == 0:
            if len(SELECTION_PORBABILITY[i]) != SELECTION_COUNT[i]:
                print('选项数量和所填的概率对不上')
                exit()
            index = probability_index(SELECTION_PORBABILITY[i]) + 1

        #多选
        elif QUESTION_TYPE[i] == 1:
            if len(SELECTION_PORBABILITY[i]) != SELECTION_COUNT[i]:
                print('选项数量和所填的概率对不上')
                exit()
            choices = []
            for j in range(randint(1, SELECTION_COUNT[i])):
                option = probability_index(SELECTION_PORBABILITY[i]) + 1
                choices.append(option)
            choices = list(set(choices))
            index = '|'.join(list(map(str, choices)))

        else:
            print('题目单选多选类型填写不对')
            exit()
        post_data['submitdata'] += '{}${}}}'.format(i + 1, index)

    post_data['submitdata'] = post_data['submitdata'][:-1]
    return post_data


def linkage_data():
    pass