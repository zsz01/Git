import time
from getpass import getpass
from os import system
import numpy
import matplotlib.pyplot as plt

class student:
    def __init__(self,Name,Class,ID,Grade):
        self.Name = Name
        self.Class = Class
        self.ID = ID
        self.Grade = Grade
    def show(self):
        print('%s\t%s\t%s\t%d' % (self.Name, self.Class, self.ID, self.Grade))

def showlist():
    global opt
    system('cls')
    print('------------------------')
    print('西安交通大学学籍管理系统     ')
    print('------------------------')
    print('1 - 查看学生成绩')
    print('2 - 修改学生成绩')
    print('3 - 添加学生成绩')
    print('4 - 删除学生成绩')
    print('5 - 学生成绩分析')
    print('6 - 更改系统密码')
    print('7 - 退出管理系统')
    print('------------------------')
    while True:
        opt = input()
        if opt == '1' or opt == '2' or opt == '3' or \
        opt == '4' or opt == '5' or opt == '6' or opt =='7':
            break
    opt = int(opt)

def loadinfo():
    global info
    global key
    data = open('info.txt', 'r', encoding='UTF-8').read()
    data = data.split('\n')
    key = data[0]
    data.pop(0)
    for stu in data:
        stu = stu.split('\t')
        try:
            info.append(student(stu[0],stu[1],stu[2],int(stu[3])))
        except IndexError:
            pass

def init():
    global info
    global key
    loadinfo()
    system('cls')
    print('------------------------')
    print('西安交通大学学籍管理系统     ')
    print('------------------------')
    k = getpass('请输入管理员密码:')
    while k != key:
        system('cls')
        print('------------------------')
        print('西安交通大学学籍管理系统     ')
        print('------------------------')
        k = getpass('密码错误，重新输入:')
    print('登陆成功!')
    time.sleep(1)

def look():
    global info
    opt = 0
    while(opt != 3):
        system('cls')
        print('------------------------')
        print('西安交通大学学籍管理系统     ')
        print('------------------------')
        print('<查看学生成绩>')
        print('1 - 按成绩升序')
        print('2 - 按成绩降序')
        print('3 - 按学生姓名查找')
        print('4 - 按学生学号查找')
        print('5 - 返回')
        print('------------------------')
        while True:
            opt = input()
            if opt == '1' or opt == '2' or opt == '3' or opt == '4' or opt == '5':
                break
        opt = int(opt)
        if opt == 1:
            info.sort(key = lambda x : x.Grade)
        elif opt == 2:
            info.sort(key = lambda x : x.Grade, reverse= True)
        elif opt == 3:
            name = input('请输入学生姓名:')
            for s in info:
                if s.Name == name:
                    s.show()
                    system('pause')
                    return
            print('未找到该学生！')
            system('pause')
            return
        elif opt == 4:
            id = input('请输入学生学号:')
            for s in info:
                if s.ID == id:
                    s.show()
                    system('pause')
                    return
            print('未找到该学生！')
            system('pause')
            return
        else:
            return
        system('cls')
        for stu in info:
            stu.show()
        system('pause')

def revise():
    system('cls')
    global info
    print('------------------------')
    print('西安交通大学学籍管理系统     ')
    print('------------------------')
    print('<修改学生成绩>')
    name = input('请输入学生姓名:')
    flag = True
    for s in info:
        if s.Name == name:
            flag = False
            s.show()
            grade = int(input("请输入修改后的成绩:"))
            s.Grade = grade
            print('修改后的学生信息:')
            s.show()
            break
    if flag == True:
        print('未找到该学生！')
    system('pause')

def add():
    system('cls')
    global info
    print('------------------------')
    print('西安交通大学学籍管理系统     ')
    print('------------------------')
    print('<添加学生成绩>')
    Name = input('请输入学生姓名:')
    Class = input('请输入学生班级:')
    ID = input('请输入学生学号:')
    Grade = int(input('请输入学生成绩:'))
    for s in info:
        if s.Name == Name:
            print('该学生成绩已经登记！')
            system('pause')
            return
    info.append(student(Name,Class,ID,Grade))
    print('添加的学生成绩信息如下:')
    student(Name, Class, ID, Grade).show()
    system('pause')

def delete():
    system('cls')
    global info
    print('------------------------')
    print('西安交通大学学籍管理系统     ')
    print('------------------------')
    print('<删除学生成绩>')
    Name = input('请输入学生姓名:')
    for s in info:
        if s.Name == Name:
            print('确认删除此学生记录？(Y/N)')
            ans = input()
            if ans == 'Y' or ans == 'y':
                info.remove(s)
                print('已删除')
                system('pause')
                return
            print('已取消删除操作')
            system('pause')
            return
    print('未找到学生信息')
    system('pause')
    return

def leave():
    system('cls')
    print('------------------------')
    print('西安交通大学学籍管理系统     ')
    print('------------------------')
    print('<退出管理系统>')
    with open('info.txt','w', encoding='utf-8') as file:
        file.write(key)
        file.write('\n')
        for s in info:
            ss = s.Name + '\t' + s.Class + '\t' + s.ID + '\t' + str(s.Grade) + '\n'
            file.write(ss)
    system('cls')

def change():
    global key
    system('cls')
    print('------------------------')
    print('西安交通大学学籍管理系统     ')
    print('------------------------')
    print('<更改系统密码>')
    cert = getpass('请输入原密码:')
    if cert != key:
        print('密码错误，更改密码失败')
        system('pause')
        return
    cert = getpass('请输入新密码:')
    key = cert
    print('成功修改密码')
    system('pause')

def analyse():
    global key
    system('cls')
    print('------------------------')
    print('西安交通大学学籍管理系统     ')
    print('------------------------')
    print('<学生成绩分析>')
    print('1 - 饼图')
    print('2 - 柱状图')
    print('3 - 文字信息')
    print('4 - 返回')
    print('------------------------')

    sizes = [0,0,0,0,0]
    for s in info:
        if s.Grade >= 90:
            sizes[0] += 1
        elif s.Grade >= 80:
            sizes[1] += 1
        elif s.Grade >= 70:
            sizes[2] += 1
        elif s.Grade >= 60:
            sizes[3] += 1
        else:
            sizes[4] += 1

    labels = '90-100', '80-89', '70-79', '60-69', '0-59'
    colors = 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'pink'
    explode = 0, 0, 0, 0.1, 0
    plt.rcParams['font.sans-serif'] = ['SimHei']

    opt = int(input())
    if opt == 1:
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%2.2f%%', shadow=True, startangle=30)
        plt.axis('equal')
        plt.title('2015级西安交通大学学生平均成绩分析\n')
        plt.show()
    elif opt == 2:
        plt.bar(labels, sizes, color='g', width=0.2)
        plt.title('2015级西安交通大学学生平均成绩分析')
        plt.yticks(sizes)
        plt.show()
    elif opt == 3:
        sum = 0
        m = n = info[0]
        for s in info:
            if s.Grade > m.Grade:
                m = s
            if s.Grade < n.Grade:
                n = s
            sum += s.Grade
        aver = sum / len(info)
        print('平均成绩为:%.2f'%aver)
        print('最高分:%s %.1f分'%(m.Name,m.Grade))
        print('最低分:%s %.1f分' % (n.Name, n.Grade))
        print('------------------------')
        system('pause')
    else:
        return

if __name__ == '__main__':
    opt = 0
    key = ''
    info = []
    init()
    showlist()
    while(opt != 7):
        system('cls')
        if opt == 1:
            look()
        elif opt == 2:
            revise()
        elif opt == 3:
            add()
        elif opt == 4:
            delete()
        elif opt == 5:
            analyse()
        elif opt == 6:
            change()
        else:
            break
        showlist()
    leave()
