#问卷的ID
ID = 20258648

#问卷的网址
WJX_URL = "https://www.wjx.cn/jq/{}.aspx".format(ID)

#回答问卷的次数
ANSWER_TIMES = 1

#西祠IP代理网址
IP_URL = 'https://www.xicidaili.com/nn/'

#生成问卷的方式，r代表随机生成，p代表根据配置的概率生成，l代表有联动题目的生成
MODE = 'p'

#概率生成需要填充的常量
#每一题是单选还是多选，0代表单选，1代表多选
QUESTION_TYPE = [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,3,0, 0,3,3,3,3, 3]

#每一题有多少个选项
SELECTION_COUNT = [4,4,4,2,3, 3,3,3,4,5, 4,4,3,4,4, 4,4,4,0,4,  4,12,0,0,0,  0]

#每个选项的概率，是一个二维列表
SELECTION_PORBABILITY = [[50,40,5,5],[50,40,5,5],[50,40,5,5],[80,20],[70,20,10],
[60,30,10],[70,20,10],[80,10,10],[40,30,20,10],[30,40,10,10,10],
[50,40,5,5],[50,40,5,5],[50,20,30],[50,40,5,5],[50,40,5,5],
[50,40,5,5],[50,40,5,5],[50,40,5,5],[],[50,40,5,5],
[50,40,5,5],[-2],[],[95,96,97,98,99,100],[],
[]

]

#成功数量
SUCCESS_TIMES=0

answer1=["无","没有","暂时没有","暂无"]
answer2=["希望政府可以出台相应的政策法律,用以监管网购快递包装循环利用情况","菜鸟驿站在今后发展中提高服务质量,宣传包装回收利用知识","无"]
