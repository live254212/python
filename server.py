import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "127.0.0.1" # Get local machine name
port = 4000                # Reserve a port for your service.
s.bind(('',port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   c.send('Thank you for connecting')
   c.close()                
   break
