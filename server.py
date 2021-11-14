
import socket

sock = socket.socket()
sock.bind(('', 8080))
sock.listen(10)
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(10240)
    data = data.decode('utf-8')
    data = data.replace("'", "")


    if not data == "Exit":
        print(addr, data)
    if data == "Exit":
        break

conn.close()