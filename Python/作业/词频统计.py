from mylib import *
f1 = open('data1.txt','r')
tmp_str = f1.read()
f1.close()
res1 = cntword(tmp_str)

f2 = open('data2.txt','r')
tmp_str = f2.read()
f2.close()
res2 = cntword(tmp_str)

delword1 = [i[0] for i in res1]
delword2 = [i[0] for i in res2]
delword = []
cnt = 0
for word in delword1:
    if word in delword2:
        delword.append(word)
print(delword)
