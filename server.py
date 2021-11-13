import socket

sock = socket.socket()

sock.bind(('', 8080))

sock.listen(1)

conn, addr = sock.accept()
print(addr)

while True:
    data = conn.recv(5120)
    print(data)
    if not data:
        break


conn.close()