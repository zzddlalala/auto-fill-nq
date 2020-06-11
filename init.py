#问卷的ID
ID = 81435309

#问卷的网址
WJX_URL = "https://www.wjx.cn/jq/{}.aspx".format(ID)

#回答问卷的次数
ANSWER_TIMES = 10

#西祠IP代理网址
IP_URL = 'https://www.xicidaili.com/nn/'

#生成问卷的方式，r代表随机生成，p代表根据配置的概率生成，l代表有联动题目的生成
MODE = 'p'

#概率生成需要填充的常量
#每一题是单选还是多选，0代表单选，1代表多选,2代表排序，3代表填空,4代表矩阵
QUESTION_TYPE = [0,0,0,0,0, 0,0,0,0,0, 0]

#每一题有多少个选项
SELECTION_COUNT = [2,4,4,4,4, 4,5,2,3,3, 5]

#每个选项的概率，是一个二维列表
SELECTION_PORBABILITY = [
[30,70],[20,30,40,10],[5,20,60,15],[50,30,10,10],[10,5,55,30],
[10,40,30,20],[40,20,10,20,10],[70,30],[30,50,20],[50,20,30],
[10,10,20,50,10]
]

#成功数量
SUCCESS_TIMES = 0
