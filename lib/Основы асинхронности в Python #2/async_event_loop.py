                                                #Основы асинхронности в Python #2: Асинхронность с простыми функциями. Событийный цикл.
import socket                                                                   #это пара домен + порт domain:port
from select import select                                                       #системная функция для мониторинга изменений состояний файловых объектов из сокетов
                                                                                #(файловый дескриптор - номер файла)

to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)               #субъект сервера
                                                                                #AF_INET - адресс фэмэли, SOCK_STREAM - поддержка работы tcp
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)             #
server_socket.bind(('localhost', 5000))                                         #
server_socket.listen()

def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()                                #accept принимает входящие подключения, и возвращает socket object и address info
    print("Connection from:", addr)
    to_monitor.append(client_socket)                                            #добавим клиентский сокет для мониторинга (их становится 2)

def send_message(client_socket):
    request = client_socket.recv(4096)                                          #клиентский сокет принимает сообощение

    if request:                                                                 #если запрос                                                            
        response = 'Hello\n'.encode()
        client_socket.send(response)                                            #буфер отправки
    else:                                                                       #если сообщений нет, закрываем сокет
        client_socket.close()

def event_loop():
    while True:

        ready_to_read, _, _ = select(to_monitor, [], [])                        #не нужные переменные идут в _ / 1й аргумент для чтения, 2й для записи 3й - ошибки

        for sock in ready_to_read:                                              #для каждого сокета(sock) в ready_to_read
            if sock is server_socket:                                           #если сокет является серверным, тогда 
                accept_connection(sock)                                         #вызывается метод accept_connection и передается в него sock
            else:
                send_message(sock)

if __name__ == "__main__":
    to_monitor.append(server_socket)                                            #передаем первый аргумент список объектов доступных для чтения
    event_loop()

    #теперь программа работает асинхронно в одном потоке
    #отредактировали скрипт таким образом, что основные функции стали независимыми друг от друга и их можно вызывать в любом порядке
    #момент когжа мы хотим их вызвать определяется в event_loop()
    #select делает выборку из списков на предмет готовности для чтения, если готовы, то идут в список
    #если серверный сокет, то передаём на подключение accept_connection(sock)
    #если клиентский сокет, то передаём в ф. send_message(sock)