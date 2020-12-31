import socket
#locking for server 
ClientSocket = socket.socket()
host = '172.99.0/24'
port = 13117
print('Client started, listening for offer requests...')
try:
    #connect
    ClientSocket.connect((host, port))
    print('Received offer from '+host+ ', attempting to connect...')
except socket.error as e:
    print(str(e))

#Game mode
Response = ClientSocket.recv(1024)
ClientSocket.send(str.encode('teamA'))
while True:
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))
    Input = input('')
    ClientSocket.send(str.encode(Input))
   
    
ClientSocket.close()