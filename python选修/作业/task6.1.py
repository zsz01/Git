#自定义复数类，实例成员为实部和虚部，构造函数将复数初始化为0+0j,
#编写相应的成员函数实现复数的求模、显示和设置实部虚部，重载加、减乘实现复数的加、减乘运算。
#编写主程序，定义复数对象，进行复数设置、运算和显示操作。
import math
class Complex:
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag
    def __add__(self, num):
        r = self.real + num.real
        i = self.imag + num.imag
        return Complex(r,i)
    def __sub__(self, num):
        r = self.real - num.real
        i = self.imag - num.imag
        return Complex(r,i)
    def __mul__(self, num):
        r = self.real * num.real - self.imag * num.imag
        i = self.real * num.imag + self.imag * num.real
        return Complex(r,i)
    def __truediv__(self, num):
        r = (self.real * num.real + self.imag * num.imag)/(num.real ** 2 + num.imag ** 2)
        i = (self.imag * num.real - self.real * num.imag)/(num.real ** 2 + num.imag ** 2)
        return Complex(r,i)
    def length(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)
    def setReal(self,real):
        self.real = real
    def setImag(self,imag):
        self.imag = imag
    def show(self):
        if self.imag < 0:
            print("%d%di"%(self.real,self.imag))
        else:
            print("%d+%di"%(self.real,self.imag))

a = Complex()
b = Complex(2,2)
a.show()
b.show()

a.setReal(1)
a.setImag(1)
a.show()
print(a.length(),b.length())

(a+b).show()
(a-b).show()
(a*b).show()
(a/b).show()
