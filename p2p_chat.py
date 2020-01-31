import sys
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time

STRATEGY = sys.argv[1] #accept or connect
PORT = int(sys.argv[2])

sock = socket(AF_INET, SOCK_STREAM)


if STRATEGY == 'accept':
    print(f"Принимаем соединения на порт {PORT}")
    sock.bind(('localhost', PORT))
    sock.listen(1)
    sock, addr = sock.accept()
    print(f"Установлено соединение с {addr}")

    # while True:
    #     a = sock.recv(4096)
    #     print(a.decode())
     
    

elif STRATEGY == 'connect':
    print(f"Отправляем соединение на адрес {PORT}")
    sock.connect( ('localhost', PORT))
    print(f"Соединение установлено")
    # while True:
    #     # a = input()
    #     sock.send(a.encode())
    #     if sock.send(a.encode() == ''):
    #         sock.close()
else:
    raise Exception("Неправильный аргумент, пишите p2p_chat accept/connect")

def accept():
    while True:
        a = sock.recv(4096)
        print(a.decode())

def connect():
    while True:
        sock.send(input().encode())

t0 = Thread(target = accept)
t1 = Thread(target = connect)

t0.start()
t1.start()

t0.join()
t1.join()
# print("Starting programs")
# t0 = Thread(target=loop, args=(2,0))  #(STEP_SIZE = 2, ELEMENT_IN_STEP = 0) 
# t1 = Thread(target=loop, args=(2,1))
# print("Starting t0")
# t0.start()
# print("Starting t1")
# t1.start()
