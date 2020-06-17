#问卷的ID
ID = 82115262

#问卷的网址
WJX_URL = "https://www.wjx.cn/jq/{}.aspx".format(ID)

#回答问卷的次数
ANSWER_TIMES = 40

#西祠IP代理网址
IP_URL = 'https://www.xicidaili.com/nn/'

#生成问卷的方式，r代表随机生成，p代表根据配置的概率生成，l代表有联动题目的生成
MODE = 'p'

#概率生成需要填充的常量
#每一题是单选还是多选，0代表单选，1代表多选,2代表排序，3代表填空,4代表矩阵
QUESTION_TYPE = [0,0,0,0,3, 0,0,0,3,2, 0,0,1,3]

#每一题有多少个选项
SELECTION_COUNT = [2,4,6,5,0, 4,5,2,0,6, 2,2,4,0]

#每个选项的概率，是一个二维列表
SELECTION_PORBABILITY = [
    [0,100],[0,40,50,10],[10,30,0,20,30,10],[20,20,30,20,10],["苏州","武汉","成都","杭州"],
    [40,30,20,10],[10,40,30,10,10],[60,40],["迪奥","香奈儿","LV","Gucci","Prada"],['1','2','3','4','5','6'],
    [40,60],[70,30],[30,70,80,60],[]
]

#成功数量
SUCCESS_TIMES = 0
