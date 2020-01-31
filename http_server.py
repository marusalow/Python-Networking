from socket import socket, AF_INET, SOCK_STREAM

server = socket(AF_INET, SOCK_STREAM)

server.bind (('0.0.0.0', 80) )                                 #80 - Порт Http
server.listen(15)                                              #15 - количество получений одновременно
connection, addr = server.accept()

print(f'Установлено соединение с адресса {addr}')

data = connection.recv(4096)
print(f"Принял данные \n {data.decode()}")

html = '<h1>hello world</h1>'
data = (
    "HTTP/1.1 200 OK\n"
    "Date: Wed, 11 Feb 2009 11:20:59 GMT\n"
    "Server: Apache\n"
    "X-Powered-By: PHP/5.2.4-2ubuntu5wm1\n"
    "Last-Modified: Wed, 11 Feb 2009 11:20:59 GMT\n"
    "Content-Language: ru\n"
    "Content-Type: text/html; charset=utf-8\n"
    "Content-Length: " + str(len(html)) + "\n"
    "Connection: close\n"
    "\n"
    + html    
).encode()

connection.send(data)
connection.close()