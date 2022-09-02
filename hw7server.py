import socket, threading
from time import sleep
from concurrent import futures as cf

def message(conn, addr):
    while True:
        for address in clients:
            if address==conn:
                data = conn.recv(1024)
                if not data:
                    break
                for i in range(len(clients)):
                    if clients[i] != conn:
                        print(f'from <{addr}> message: {data}')
                        msg = data.decode()
                        clients[i].send((f'from <{addr}> message: {msg}').encode())
    #conn.close()

host = ''
port = 55555
clients = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))  #  Привязывает сокет к адресу address (инициализирует IP-адрес и порт). Сокет не должен быть привязан до этого.
s.listen(10)           #  Переводит сервер в режим приема соединений. Параметр``backlog (int)`` – количество соединений, которые будет принимать сервер.
print('server start')
while True:
    conn, addr = s.accept()
    print(f'<{addr}> conected')
    clients.append(conn)
    threading.Thread(target=message, args=[conn, addr]).start()

s.close()
