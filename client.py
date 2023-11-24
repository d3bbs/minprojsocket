import socket


ip="localhost"
port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))
print("Connected to server at port ",ip ,port)
rec_message=s.recv(1024)
rec_message=rec_message.decode()
print("Server says: ", rec_message)

if rec_message=="HelloC":
    client_message="HelloS"
    client_message=client_message.encode()
    s.send(client_message)
else:
    print("Server did not say HelloC")
    s.close()
    exit()
    
while True:
    command=input("Enter command: (POW,SQRT,BYE): \n")
    if command=='POW'or command=='SQRT':
        num=input("Enter number: \n")
        client_message=command+"="+num
        client_message=client_message.encode()
        s.send(client_message)
        
        rec_message=s.recv(1024)
        rec_message=rec_message.decode()
        print("Server says: ", rec_message)
    elif command=='BYE':
        s.close()
        break
    else:
        print("Invalid command")