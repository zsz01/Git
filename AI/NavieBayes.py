# 数据集/训练集: 北京2010 - 2015年的天气信息
# 输入data(湿度, 气压),返回最可能处于的季节
# 湿度分为10组(0-100)
# 气压分为5组

# s[1],s[2],s[3],s[4]代表四季

from handle import getData

class info:
    def __init__(self):
        self.cnt = 0
        self.cnthumi = [0 for i in range(10 + 1)]
        self.cntpres = [0 for i in range(5 + 1)]

def init(data):
    s = []
    for i in range(5):
        s.append(info())
    for d in data:
        # 每个季节出现的次数
        s[int(d[0])].cnt += 1
        # 此季节每个湿度出现的次数
        s[int(d[0])].cnthumi[int(d[1])] += 1
        # 此季节每个气压出现的次数
        s[int(d[0])].cntpres[int(d[2])] += 1
    return s

def NavieBayes(s, t):
    pmax = 0
    season = 0
    length = 0
    for i in s:
        length += i.cnt

    for i in range(1,5):
        temp = s[i].cnt / length * s[i].cnthumi[t[0]] / sum(s[i].cnthumi) *\
               s[i].cntpres[t[1]] / sum(s[i].cntpres)
        if temp > pmax:
            pmax = temp
            season = i
    return season


if __name__ == '__main__':
    data = getData(r'C:\Users\heyon\Desktop\handle\train.txt')
    s = init(data)
    train = getData(r'C:\Users\heyon\Desktop\handle\train.txt')
    cnt = 0
    cnt_equal = 0
    for i in train:
        cnt += 1
        temp = [i[1],i[2]]
        if i[0] == NavieBayes(s,temp):
            cnt_equal += 1

    print('在测试集上测试的正确率为:%.2f'%(cnt_equal/cnt * 100),end = '%')