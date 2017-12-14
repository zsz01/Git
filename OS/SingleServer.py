import socket
import math
from threading import Thread


def f(cs, name):
    cs.send("Log in Server！".encode('utf-8'))
    msg = cs.recv(1024).decode('utf-8')
    while msg != 'bye':
        ans = str(math.factorial(int(msg)))
        cs.send(ans.encode('utf-8'))
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
        client_thread = Thread(target=f, args=(cs, name))
        client_thread.start()


if __name__ == '__main__':
    initSever(socket.gethostname(), 5458)
