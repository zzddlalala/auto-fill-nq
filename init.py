#问卷的ID
ID = 85036895

#问卷的网址
WJX_URL = "https://www.wjx.cn/jq/{}.aspx".format(ID)

#回答问卷的次数
ANSWER_TIMES =105

#西祠IP代理网址
IP_URL = 'https://www.kuaidaili.com/free/inha/'

#生成问卷的方式，r代表随机生成，p代表根据配置的概率生成，l代表有联动题目的生成
MODE = 'p'

#概率生成需要填充的常量
#每一题是单选还是多选，0代表单选，1代表多选,2代表排序，3代表填空,4代表矩阵,5代表多项填空
QUESTION_TYPE = [0,0,0,0,0, 1,0]

#每一题有多少个选项
SELECTION_COUNT = [3,3,2,4,4, 4,2]

#每个选项的概率，是一个二维列表
SELECTION_PORBABILITY = [
    [65,30,5],[86,12,2],[15,85],[30,14,50,6],[33,46,16,5],
    [50,15,63,5],[75,25]
]

#成功数量
SUCCESS_TIMES = 0
