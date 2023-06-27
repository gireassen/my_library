                                                #Основы асинхронности в Python #3: Асинхронность на колбэках.
import socket                                                                                               #это пара домен + порт domain:port
import selectors                                                                                            #системная функция для мониторинга изменений состояний файловых объектов из сокетов
                                                                                                            #(файловый дескриптор - номер файла)

selector = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                       #субъект сервера
                                                                                                            #AF_INET - адресс фэмэли, SOCK_STREAM - поддержка работы tcp
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)                                     #
    server_socket.bind(('localhost', 5000))                                                                 #
    server_socket.listen()

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)           #register принимает 3 аргумента: файловый объект, events - событие, которое нас интересует и data - любые связанные данные с этим

def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()                                                            #accept принимает входящие подключения, и возвращает socket object и address info
    print("Connection from:", addr)
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)
    

def send_message(client_socket):
    request = client_socket.recv(4096)                                                                      #клиентский сокет принимает сообощение

    if request:                                                                                             #если запрос                                                            
        response = 'Hello\n'.encode()
        client_socket.send(response)                                                                        #буфер отправки
    else:                                                                                                   #если сообщений нет, закрываем сокет
        selector.unregister(client_socket)
        client_socket.close()

def event_loop():
    while True:
        pass

if __name__ == "__main__":
    event_loop()