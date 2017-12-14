import socket
from threading import Thread


def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * factorial(x - 1)
#执行线程的函数


def function(msg, cs):
    ans = str(factorial(int(msg))).encode('utf-8')
    try:
        cs.send(ans)
    except:
        pass

#分配输入的函数


def f(cs, name):
    cs.send("Log in Server！".encode('utf-8'))
    msg = cs.recv(1024).decode('utf-8')
    while msg != 'bye':
      	#为用户的每个输入分配一个线程
        calculate_thread = Thread(target=function, args=(msg, cs))
        calculate_thread.start()
        msg = cs.recv(1024).decode('utf-8')
    print('Client', name, 'log out')
    cs.close()


def initSever(host, port):
    ss = socket.socket()
    ss.bind((host, port))
    print('Waiting for connecting...')
    ss.listen()
    num = 1
    while True:
        cs, addr = ss.accept()
        print('Connecting to', addr)
        name = str(num)
        num += 1
        #为每个用户分配一个线程
        client_thread = Thread(target=f, args=(cs, name))
        client_thread.start()


if __name__ == '__main__':
    initSever(socket.gethostname(), 5458)
