
def isleap(year):
    return (year%4==0 and year%100!=0) or (year%400==0)

def getMonthName(month):
    monthNames = ['','January','February','March',
        'April','May','June','July','August',
        'September','October','November','December']
    return monthNames[month]

def getMonthDays(year,month):
    L = [1,3,5,7,8,10,12]
    if month in L:
        return 31
    elif month == 2:
        if isleap(year):
            return 29
        else:
            return 28
    else:
        return 30

def getDays(year,month):
    days = 0
    for i in range(1,year):
        if isleap(i):
            days += 366
        else:
            days += 365
    for i in range(1,month):
        days += getMonthDays(year,i)
    return days + 1

def getWeekday(year,month):
    d = getDays(year,month)
    return d % 7

def show(year,month):
    print('        ',getMonthName(month),year)
    print('  Sun Mon Tue Wed Thu Fri Sat')
    k = getWeekday(year,month)
    for i in range(k):
        print('    ',end = '')
    daysofmonth = getMonthDays(year,month)
    for i in range(1,daysofmonth+1):
        print('%4d'%i,end = '')
        if((k+i)%7 == 0):
            print()

date = input().split(' ')
year, month = int(date[0]),int(date[1])
show(year,month)
