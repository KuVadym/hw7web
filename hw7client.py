import socket, threading
from time import sleep

def incoming(s):
    while True:
        message = s.recv(2048)
        print(f'{message.decode()}')


with socket.socket() as s:
    s.connect(('127.0.0.1', 55555))
    print(b'welcome to chat')
    threading.Thread(target=incoming, args=[s], daemon=True).start()
    while True:
            command = input ('')
            if command == 'stop':
                break
            s.sendall(command.encode())



