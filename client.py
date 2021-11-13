import socket

sock = socket.socket()
sock.connect(('localhost', 8080))
s = input("Введите сообщение: ")
sock.send(bytes(s, encoding='utf-8'))

data = sock.recv(5120)
sock.close()

print(data)


bytes(s, encoding='utf-8')