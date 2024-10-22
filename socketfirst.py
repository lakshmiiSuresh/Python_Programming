# # server that waits for connections and shows a message when someone connects to it.
# # import socket 
# # # s = socket(module).socket(class)
# # s = socket.socket() #socket inte akthe class inu instance create cheithu
# # s.bind(("localhost",999))#ip address, portnumber
# # s.listen()
# # print("waiting for connection")
# # while True:
# #     cc,address = s.accept()
#     # print("connected",address) #address contain ip address and port number of client
    

# # import socket 
# # s = socket.socket()
# # s.bind(("localhost",999))
# # s.listen()
# # print("waiting for connection")
# # while True:
# #     cc,address = s.accept()
# #     print("connected",address)
# #     cc.send("thank you for connecting".encode())
    


# # import socket 
# # s = socket.socket()
# # s.bind(("localhost",999))
# # s.listen()
# # print("waiting for connection")
# # while True:
# #     cc,address = s.accept()
# #     name = cc.recv(100).decode()
# #     print("connected",address,name)
# #     cc.send("thank you for connecting".encode())
    

# import socket 
# s = socket.socket() 
# s.bind(("localhost",999))
# s.listen()
# print("waiting for connection")
# while True:
#     cc,address = s.accept()
#     print("connected",address)
#     while True:
#         server_msg = input("Server: ")
#         cc.send(server_msg.encode())
#         x = cc.recv(100).decode()
#         print("Lakshmi:",x)
        

    
import socket 
s = socket.socket()
s.bind(("localhost",999))
s.listen()
print("waiting for connection")
while True:
    cc,address = s.accept()
    print("connected",address)