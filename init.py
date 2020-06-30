#问卷的ID
ID = 82444551

#问卷的网址
WJX_URL = "https://www.wjx.cn/jq/{}.aspx".format(ID)

#回答问卷的次数
ANSWER_TIMES =45

#西祠IP代理网址
IP_URL = 'https://www.kuaidaili.com/free/inha/'

#生成问卷的方式，r代表随机生成，p代表根据配置的概率生成，l代表有联动题目的生成
MODE = 'p'

#概率生成需要填充的常量
#每一题是单选还是多选，0代表单选，1代表多选,2代表排序，3代表填空,4代表矩阵,5代表多项填空
QUESTION_TYPE = [0,0,0,0,0, 0,0,0,0,0, 0,0,1,1,0, 1,1,0,1,4]

#每一题有多少个选项
SELECTION_COUNT = [2,3,2,2,5, 6,2,4,5,4, 3,3,5,5,2, 4,4,5,6,2]

#每个选项的概率，是一个二维列表
SELECTION_PORBABILITY = [
    [0,100],[20,60,20],[90,10],[80,20],[10,30,35,20,5],
    [10,20,30,10,20,10],[55,45],[10,40,30,20],[0,80,0,20,0],[20,40,30,10],
    [10,60,30],[30,30,40],[60,60,30,50,40],[60,40,50,60,50],[20,80],
    [30,60,40,10],[50,70,50,10],[10,10,40,30,10],[40,60,10,10,10,0],
    [[20,80],[60,40],[90,10]]
]

#成功数量
SUCCESS_TIMES = 0
