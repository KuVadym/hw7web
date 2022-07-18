import socket, threading
from time import sleep
from concurrent import futures as cf

def message(conn, addr):
    while True:
        for address in clients:
            data = conn.recv(1024)
            if not data:
                break
            if address != conn:
                print(f'from <{addr}> message: {data}')
                msg = data.decode()
                address.send((f'from <{addr}> message: {msg}').encode())
    #conn.close()

host = ''
port = 55555
clients = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))  #  Привязывает сокет к адресу address (инициализирует IP-адрес и порт). Сокет не должен быть привязан до этого.
s.listen(10)           #  Переводит сервер в режим приема соединений. Параметр``backlog (int)`` – количество соединений, которые будет принимать сервер.
print('server start')
#with cf.ThreadPoolExecutor(10) as client_pool:
while True:
    conn, addr = s.accept()
    print(f'<{addr}> conected')
    clients.append(conn)
    threading.Thread(target=message, args=[conn, addr]).start()
    #client_pool.submit(message, conn, addr)
    #conn.send(b'I see your message')

s.close()


# cd C:\Users\kuzik\Desktop\Vadym
# python hw7.py
# python hw7c.py