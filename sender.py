from socket import socket, AF_INET, SOCK_STREAM

sender = socket(AF_INET, SOCK_STREAM) #ОТПРАВИТЕЛЬ
sender.connect(('192.168.2.74', 90))
print("Установлено соединение")
sender.send('Ваня ПРИВЕТ!'.encode())

sender.close()
