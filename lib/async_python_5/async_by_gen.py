                                                #Основы асинхронности в Python #5: Асинхронность на генераторах
import socket
from select import select

tasks = []

to_read = {}
to_write = {}

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #субъект сервера
                                                                            #AF_INET - адресс фэмэли, SOCK_STREAM - поддержка работы tcp
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     #
    server_socket.bind(('localhost', 5000))                                 
    server_socket.listen()

    while True:
        
        yield ("read", server_socket)
        client_socket, _ = server_socket.accept()
        tasks.append(client(client_socket))


def client(client_socket):
    while True:
        
        yield ("read", client_socket)
        request = client_socket.recv(4096)                              #клиентский сокет принимает сообощение

        if not request:                                                 #если нет запроса
            break
        else:                                                           #если пришёл запрос
            response = 'Hello\n'.encode()
            
            yield ("write", client_socket)
            client_socket.send(response)                                #буфер отправки

    client_socket.close()

def event_loop():
    while any([tasks, to_read, to_write]):
        # наполняем генераторами
        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)
            reason, sock = next(task)  #("read", client_socket) или ("write", client_socket)
            if reason == 'read':
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task

        except StopIteration:
            print('Done')

tasks.append(server())
event_loop()

# мы преобразовали функции в генераторы и эти генераторы отдают нам кортежи
# где первый эл-т кортежа - филтрующий признак, по которому мы определяем куда пойдёт сокет, который второй в кортеже
# 
# #