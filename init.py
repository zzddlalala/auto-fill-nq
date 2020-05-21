#问卷的ID
ID = 78377947

#问卷的网址
WJX_URL = "https://www.wjx.cn/jq/{}.aspx".format(ID)

#回答问卷的次数
ANSWER_TIMES = 10

#西祠IP代理网址
IP_URL = 'https://www.xicidaili.com/nn/7'

#生成问卷的方式，r代表随机生成，p代表根据配置的概率生成，l代表有联动题目的生成
MODE = 'p'

#概率生成需要填充的常量
#每一题是单选还是多选，0代表单选，1代表多选
QUESTION_TYPE = [0,0,0,0,0, 0,1,1]

#每一题有多少个选项
SELECTION_COUNT = [2,5,5,6,3, 2,5,5]

#每个选项的概率，是一个二维列表
SELECTION_PORBABILITY = [[40,60],[10,20,30,30,10],[5,15,30,40,10],[2,8,40,5,40,5],[10,30,60], [90,10],[85,85,85,75,17],[67,50,80,75,11]]

#成功数量
SUCCESS_TIMES=0
