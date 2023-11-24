import socket
import math

ip= "localhost"
port= 12345
buffersize= 1024
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip,port))
s.listen()
print("Server is listening at port", port)
client_sock, addr= s.accept()
print("Client connected with address: ", addr)

srv_message= "HelloC"
srv_message= srv_message.encode()
client_sock.send(srv_message)    
#srv sending message to client

clientmessage= client_sock.recv(buffersize)
clientmessage= clientmessage.decode()
print("Client says: ", clientmessage)
    
while True:
    clientmessage= client_sock.recv(buffersize)
    clientmessage= clientmessage.decode()
    print("Client says: ", clientmessage)
    
    if clientmessage.startswith("POW"):
        num= int(clientmessage.split("=")[1])
        result= math.pow(num,num)
        result= str(result)
        result= result.encode()
        client_sock.send(result)
        
    elif clientmessage.startswith("SQRT"):
        num= int(clientmessage.split("=")[1])
        result= math.sqrt(num)
        result= str(result)
        result= result.encode()
        client_sock.send(result)
    elif clientmessage=="BYE":
        client_sock.close()
        s.close()
        break
    else:
        print("Invalid command")
        