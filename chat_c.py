
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345               # Reserve a port for your service.

s.connect((host, port))
while True:
    input = raw_input("Enter data to be sent")
    s.send(input)    
    m=s.recv(1024)
    print m
     
    s.close()

