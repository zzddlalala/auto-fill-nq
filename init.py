#问卷的ID
ID = 81242605

#问卷的网址
WJX_URL = "https://www.wjx.cn/jq/{}.aspx".format(ID)

#回答问卷的次数
ANSWER_TIMES = 100

#西祠IP代理网址
IP_URL = 'https://www.xicidaili.com/nn/'

#生成问卷的方式，r代表随机生成，p代表根据配置的概率生成，l代表有联动题目的生成
MODE = 'p'

#概率生成需要填充的常量
#每一题是单选还是多选，0代表单选，1代表多选,2代表排序，3代表填空
QUESTION_TYPE = [1]

#每一题有多少个选项
SELECTION_COUNT = [5]

#每个选项的概率，是一个二维列表
SELECTION_PORBABILITY = [
[20,40,30,10,0]
]

#成功数量
SUCCESS_TIMES=0
