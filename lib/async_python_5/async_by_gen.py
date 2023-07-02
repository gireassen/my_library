                                                #Основы асинхронности в Python #5: Асинхронность на генераторах
import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #субъект сервера
                                                                            #AF_INET - адресс фэмэли, SOCK_STREAM - поддержка работы tcp
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     #
    server_socket.bind(('localhost', 5000))                                 
    server_socket.listen()

    while True:
        client_socket, _ = server_socket.accept()
        client(client_socket)

def client(client_socket):
    while True:
        request = client_socket.recv(4096)                              #клиентский сокет принимает сообощение

        if not request:                                                 #если нет запроса
            break
        else:                                                           #если пришёл запрос
            response = 'Hello\n'.encode()
            client_socket.send(response)                                #буфер отправки

    client_socket.close()

if __name__ == "__main__":
    server()