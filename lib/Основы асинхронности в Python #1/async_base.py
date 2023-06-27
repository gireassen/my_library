#Основы асинхронности в Python #1: Введение
import socket #это пара домен + порт domain:port

def function_1():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #субъект сервера
                                                                            #AF_INET - адресс фэмэли, SOCK_STREAM - поддержка работы tcp
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     #
    server_socket.bind(('localhost', 5000))                                 #
    server_socket.listen()

    while True:
        print("Before .accept()")
        client_socket, addr = server_socket.accept()                        #accept принимает входящие подключения, и возвращает socket object и address info
        print("Connection from:", addr)

        while True:
            print("Before .recv(4096)")
            request = client_socket.recv(4096)                              #клиентский сокет принимает сообощение

            if not request:                                                 #если нет запроса
                break
            else:                                                           #если пришёл запрос
                response = 'Hello\n'.encode()
                client_socket.send(response)                                #буфер отправки

        print('Outside inner while loop')
        client_socket.close()

# .send() - блокирующая операция. они блокируют выполнение программы, пока не закончат свою работу.
# при обращении второго клиента, ответа не поступит, он будет зациклен во втором цикле

#   чтобы принять второе подключение нужно было бы выйти из внутреннего цикла, чтобы попасть на вторую итерацию внешнего цикла
#   нужно передавать контроль выполнение команд и код(менеджер) который бы рулил процессом (Называется event loop(бытийным циклом или циклом событий))

# асинхронный код можно писать с:
# 1) callback 
# 2)генераторов corutine 
# 3)с синаксисом async await
# без использования сторонних библиотек


if __name__ == "__main__":
    function_1()
