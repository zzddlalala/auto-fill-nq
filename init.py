#问卷的ID
ID = 80531957

#问卷的网址
WJX_URL = "https://www.wjx.cn/jq/{}.aspx".format(ID)

#回答问卷的次数
ANSWER_TIMES = 150

#西祠IP代理网址
IP_URL = 'https://www.xicidaili.com/nn/'

#生成问卷的方式，r代表随机生成，p代表根据配置的概率生成，l代表有联动题目的生成
MODE = 'p'

#概率生成需要填充的常量
#每一题是单选还是多选，0代表单选，1代表多选
QUESTION_TYPE = [0,0,1,0,0, 0,0,0,3,0, 0,0,1,1,1, 0,1,0]

#每一题有多少个选项
SELECTION_COUNT = [4,2,6,3,4, 3,3,3,0,3, 3,3,10,10,11, 2,7,7]

#每个选项的概率，是一个二维列表
SELECTION_PORBABILITY = [[40,30,20,10],[40,60],[10,30,20,20,10,10],[80,10,10],[30,50,10,10],
[30,50,20],[40,30,30],[50,30,20],["","","","",""],[30,50,20],
[70,20,10],[70,20,10],[30,30,20,20,10, 10,10,10,10,10],[10,40,40,20,20, 10,10,10,10,10],[40,40,30,30,20, 10,20,10,10,10],
[50,50],[10,20,20,10,10, 20,20],[10,20,20,10,10, 20,40]
]

#成功数量
SUCCESS_TIMES=0
