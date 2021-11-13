import socket

sock = socket.socket()

sock.bind(('', 8080))

sock.listen(1)

conn, addr = sock.accept()

while True:
    data = conn.recv(5120)
    if not data:
        break
    conn.send(data.upper())

conn.close()