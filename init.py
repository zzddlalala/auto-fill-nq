#问卷的ID
ID = 80247748

#问卷的网址
WJX_URL = "https://www.wjx.cn/jq/{}.aspx".format(ID)

#回答问卷的次数
ANSWER_TIMES = 92

#西祠IP代理网址
IP_URL = 'https://www.xicidaili.com/nn/'

#生成问卷的方式，r代表随机生成，p代表根据配置的概率生成，l代表有联动题目的生成
MODE = 'p'

#概率生成需要填充的常量
#每一题是单选还是多选，0代表单选，1代表多选
QUESTION_TYPE = [0,0,0,0,0, 0,0,0,0,0, 1,1,1,1,1, 1,3]

#每一题有多少个选项
SELECTION_COUNT = [2,5,5,5,4, 3,5,5,4,2, 4,5,6,8,7, 5,0]

#每个选项的概率，是一个二维列表
SELECTION_PORBABILITY = [[40,60],[30,40,10,10,10],[30,40,10,20,0],[10,20,30,40,0],[20,30,40,10],
[20,50,30],[20,40,20,20,0],[10,30,30,20,10],[30,40,40,0],[100,0],
[60,60,80,70],[40,30,40,50,0],[50,60,70,80,80,0],[50,60,60,50,60,70,50,60],[50,50,50,50,50,50,0],
[50,30,50,70,0],[]
]

#成功数量
SUCCESS_TIMES=0
