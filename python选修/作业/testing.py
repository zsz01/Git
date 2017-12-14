data = open('score.txt','r',encoding = 'utf-8').read()
data = data.split('\n')
result = []
for i in data:
    i = i.split('\t')
    result.append(i)
with open('score.txt','w',encoding = 'utf-8') as f:
    for i in result:
        print()
        try:
            ss = i[1] + '\t' + i[2] + '\t' + i[0] + '\t'+i[3] + '\n'
            f.write(ss)
        except Exception as e:
            print(e)
