

import socket

sock = socket.socket()
sock.connect(('localhost', 8080))
s = input("Введите код команды или наберите сообщение: ")
s = s.encode('utf-8')
sock.send(s)

data = sock.recv(1024)
sock.close()

print(data)
