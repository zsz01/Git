import socket

def chatClient():
    s = socket.socket()
    host = socket.gethostname()
    port = 5458

    s.connect((host, port))
    msg = s.recv(1024).decode('utf-8')
    while msg != 'bye':
        print('Server:',msg)
        msg = input('Client:')
        if msg == 'bye':
            print('Server:',msg)
            print('Log out Chat Server')
            s.close()
            return
        s.send(msg.encode('utf-8'))
        msg = s.recv(1024).decode('utf-8')

    print('Server:',msg)
    s.close()

chatClient()