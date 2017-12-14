a = int(input())
if a % 400 == 0:
    print('True')
else:
    if (a % 4 == 0) & (a % 100 != 0):
        print('True')
    else:
        print('False')
        
