# # import socket 
# # c = socket.socket()
# # c.connect(("localhost",999))

# # import socket 
# # c = socket.socket()
# # c.connect(("localhost",999))
# # x = c.recv(100).decode()
# # print(x)


# # import socket 
# # c = socket.socket()
# # c.connect(("localhost",999))
# # name = input("enter your name: ")
# # c.send(name.encode())
# # x = c.recv(100).decode()
# # print(x)

# import socket 
# c = socket.socket()
# c.connect(("localhost",999))
# while True:
#     x = c.recv(100).decode()
#     print("Server: ",x)
#     client_msg = input("Client: ")
#     c.send(client_msg.encode())


# # shnj qybf knoh rwhi

import socket
c = socket.socket()
c.connect(("localhost",999))