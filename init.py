#问卷的ID
ID = 81594009

#问卷的网址
WJX_URL = "https://www.wjx.cn/jq/{}.aspx".format(ID)

#回答问卷的次数
ANSWER_TIMES = 20

#西祠IP代理网址
IP_URL = 'https://www.xicidaili.com/nn/'

#生成问卷的方式，r代表随机生成，p代表根据配置的概率生成，l代表有联动题目的生成
MODE = 'p'

#概率生成需要填充的常量
#每一题是单选还是多选，0代表单选，1代表多选,2代表排序，3代表填空,4代表矩阵
QUESTION_TYPE = [3]

#每一题有多少个选项
SELECTION_COUNT = [0]

#每个选项的概率，是一个二维列表
SELECTION_PORBABILITY = [
['3}2$5}3$4}4$2}5$1}6$2}7$2}8$2}9$2}10$2}11$2}12$2}13$1}14$2}15$4}16$4}17$2}18$4}19$2}20$青海大学}21$3}22$2}23$1}24$']
]

#成功数量
SUCCESS_TIMES = 0
