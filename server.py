import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '172.1.0.144'
port = 2144
ThreadCount = 0

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))


print('Server started,listening on IP address 172.1.0.144')
ServerSocket.listen(5)

def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        
        data = connection.recv(2048)
        reply =  'Welcome to Keyboard Spamming Battle Royale.\n Group 1:\n== \n Group2:\n== \n Start pressing keys on your keyboard as fast as you can!! ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
        while True:
            data = connection.recv(2048)
            reply = 'Server Says: ' + data.decode('utf-8')
            if not data:
                break
            connection.sendall(str.encode(reply))
        connection.close()
        
    connection.close()

def first_connection(connection):
    connection.send(str.encode('Welcome to the Server\n'))
    data = connection.recv(2048)
    connection.close()
    return data.decode('utf-8','strict')

group1=[]
group2=[]
while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    teamName=first_connection
    if(ThreadCount%2==0):
        group2.append(teamName)
    else:
        group1.append(teamName)
    
    print(group1[0])
    print(group2)
ServerSocket.close()

print("hello world")