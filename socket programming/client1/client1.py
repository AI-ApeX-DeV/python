import socket
name = 'rahul'
c = socket.socket()

c.connect(("localhost", 9999))
c.send(bytes(name, 'utf-8'))
while True:
    print(c.recv(1024).decode())
