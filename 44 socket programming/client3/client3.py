import socket

c = socket.socket()
name = "sharukhali"
c.connect(("localhost", 9999))
c.send(bytes(name, 'utf-8'))
while True:
    print(c.recv(1024).decode())
    send_msg = input("Enter your message: ")
    c.send(bytes(send_msg, 'utf-8'))
