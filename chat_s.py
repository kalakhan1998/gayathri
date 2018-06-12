import socket # Import socket module

s = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345 # Reserve a port for your service.
s.bind((host, port)) # Bind to the port

s.listen(5)
# Now wait for client connection.
#status=1
l={'hey':'hello'}
while True:
	c, addr = s.accept() # Establish connection with client.

	print 'Got connection from', addr
	status=int(raw_input("enter users status"))
	k=c.recv(1024)
	if status==0:
		c.send(l[k])
	else:
		m=raw_input("enter your reply")
c.send(m)
c.close()
