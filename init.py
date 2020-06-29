#问卷的ID
ID = 83563688

#问卷的网址
WJX_URL = "https://www.wjx.cn/jq/{}.aspx".format(ID)

#回答问卷的次数
ANSWER_TIMES = 10

#西祠IP代理网址
IP_URL = 'https://www.kuaidaili.com/free/intr/'

#生成问卷的方式，r代表随机生成，p代表根据配置的概率生成，l代表有联动题目的生成
MODE = 'p'

#概率生成需要填充的常量
#每一题是单选还是多选，0代表单选，1代表多选,2代表排序，3代表填空,4代表矩阵
QUESTION_TYPE = [0,0,0,0,0]

#每一题有多少个选项
SELECTION_COUNT = [2,2,2,2,2]

#每个选项的概率，是一个二维列表
SELECTION_PORBABILITY = [
    [40,60],[40,60],[40,60],[40,60],[40,60]
]

#成功数量
SUCCESS_TIMES = 0
