def data_in():
    s = []
    while(1):
        data = input()
        if data != 'end':
            s.append(int(data))
        else:
            break
    return s

def pow(s):
    for i in range(len(s)):
        s[i] = s[i] * s[i]
    return s

def data_out(str):
    for i in range(len(str)-1):
        print(str[i],end = ' ')
    print(s[-1])

s = data_in()
s = pow(s)
data_out(s)
