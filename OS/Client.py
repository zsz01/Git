import socket

def chatClient():
    s = socket.socket()
    host = '118.126.115.149'
    port = 80

    s.connect((host, port))
    msg = s.recv(1024).decode('utf-8')
    while msg != 'bye':
        print('Server:',msg)
        msg = input('Client:')
        if msg == 'bye':
            s.close()
            return
        s.send(msg.encode('utf-8'))
        msg = s.recv(1024).decode('utf-8')
    s.close()

chatClient()