#问卷的ID
ID = 81034064

#问卷的网址
WJX_URL = "https://www.wjx.cn/jq/{}.aspx".format(ID)

#回答问卷的次数
ANSWER_TIMES = 75

#西祠IP代理网址
IP_URL = 'https://www.xicidaili.com/nn/'

#生成问卷的方式，r代表随机生成，p代表根据配置的概率生成，l代表有联动题目的生成
MODE = 'p'

#概率生成需要填充的常量
#每一题是单选还是多选，0代表单选，1代表多选,2代表排序，3代表填空,4代表矩阵
QUESTION_TYPE = [0,0,3,0,0, 0,0,1,0,1, 0,1,1,1,1]

#每一题有多少个选项
SELECTION_COUNT = [2,3,0,2,3, 3,3,4,4,4, 2,8,5,6,5]

#每个选项的概率，是一个二维列表
SELECTION_PORBABILITY = [
[75,25],[13,35,52],["2"],[44,56],[17,83,0],
[89,11,0],[10,63,27],[35,11,54,0],[23,26,51,0],[46,36,18,0],
[79,21],[67,54,55,62,65,68,71,0],[18,22,68,61,0],[67,68,51,58,50,0],[62,57,60,66,0]
]

#成功数量
SUCCESS_TIMES = 0
