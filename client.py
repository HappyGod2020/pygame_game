import socket

sock = socket.socket()
sock.connect(('localhost', 8080))
sock.send('hello, world!')

data = sock.recv(5120)
sock.close()

print(data)