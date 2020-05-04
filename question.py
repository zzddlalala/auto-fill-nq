from random import (randint, sample)


def radio(question):
    '''
    单选题
    '''

    choices = [t.text for t in question.find('label')]
    random_index = randint(0, len(choices) - 1)
    choice = choices[random_index]
    print('选项:{}'.format(choices))
    print('选择的答案:{}'.format(choice))
    print('~~~~~~~~~~~~~~~~~~~~~~')
    return random_index


def checkBox(question):
    '''
    多选题
    '''

    choices = [t.text for t in question.find('label')]
    choice_count = randint(1, len(choices))
    random_index = sample(range(1, len(choices)+1), choice_count)

    random_index_str = []
    for i in range(len(random_index)):
        random_index_str.append(str(random_index[i]))

    random_choices = [0 for i in range(len(random_index))]
    for i, r in enumerate(random_index):
        random_choices[i] = choices[r-1]
    print('选项:{}'.format(choices))
    print('选择的答案:{}'.format(random_choices))
    print('~~~~~~~~~~~~~~~~~~~~~~')
    return '|'.join(random_index_str)
   