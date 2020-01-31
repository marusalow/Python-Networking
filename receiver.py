from socket import socket, AF_INET, SOCK_STREAM
#AF_INET - IP протокол
#SOCK_STREAM - TCP - гарантирует доставку
receiver = socket(AF_INET, SOCK_STREAM) #ПОЛУЧАТЕЛЬ
#'' - IP адрес, 90 - порт
receiver.bind (('0.0.0.0', 90) ) 
receiver.listen(1) 


receiver, addr = receiver.accept()  # Готов к принятию соединения

print(f"Установлено соединение с адреса {addr}")
#recv(кол-во байт) - принимаем send
data = receiver.recv(4096)
print(f"Приемник принял данные {data.decode()}")

receiver.close()




