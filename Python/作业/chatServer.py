import socket
from threading import Thread

def chatThread(cs, name):
    cs.send("Log in Chat Server！".encode('utf-8'))
    msg = cs.recv(1024).decode('utf-8')
    while msg != 'bye':
        print('Client',name,":",msg)
        msg = input('Server:')
        if msg == 'bye':
            print('Client',name,'lost!')
            cs.close()
            return
        cs.send(msg.encode('utf-8'))
        msg = cs.recv(1024).decode('utf-8')
    print('Client', name, msg)
    print('Log out!')
    cs.close()

def initSever(host, port):
    ss = socket.socket()
    ss.bind((host,port))
    print('Waiting for connecting...')
    ss.listen()
    num = 1
    while True:
        cs, addr = ss.accept()
        print('Connecting to', addr)
        name = str(num)
        num += 1
        client_thread = Thread(target = chatThread, args = (cs, name))
        client_thread.start()

if __name__ == '__main__':
    initSever(socket.gethostname(), 5458)

