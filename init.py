#问卷的ID
ID = 80775596

#问卷的网址
WJX_URL = "https://www.wjx.cn/jq/{}.aspx".format(ID)

#回答问卷的次数
ANSWER_TIMES = 200

#西祠IP代理网址
IP_URL = 'https://www.xicidaili.com/nn/'

#生成问卷的方式，r代表随机生成，p代表根据配置的概率生成，l代表有联动题目的生成
MODE = 'p'

#概率生成需要填充的常量
#每一题是单选还是多选，0代表单选，1代表多选
QUESTION_TYPE = [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]

#每一题有多少个选项
SELECTION_COUNT = [3,2,3,2,2, 3,3,3,3,3, 3,3,3,3,3, 3,3,3,3,3]

#每个选项的概率，是一个二维列表
SELECTION_PORBABILITY = [[60,30,10],[60,40],[70,20,10],[60,40],[20,80],
[40,20,40],[80,10,10],[70,20,10],[70,20,10],[70,20,10],
[50,40,10],[70,20,10],[70,20,10],[70,20,10],[70,20,10],
[70,20,10],[70,20,10],[70,20,10],[60,20,20],[60,20,20],
]

#成功数量
SUCCESS_TIMES=0
