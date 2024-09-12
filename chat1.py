import socket
import select
from threading import *
from _thread import *
import sys
import _thread
from rearranger import *
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_address, Port)) 
server.listen(15)
list_of_clients=[]

def clientthread(conn, addr):
    conn.send(b'< server > Welcome to this chatroom!')
    while True:
            try:     
                message = conn.recv(100000)
                m=message.decode()
                z=denamer(m)
                if message:
                    message_to_send="<" + z[0] +"("+addr[0]+")> " + z[1]
                    print(message_to_send)
                    m1=message_to_send.encode()
                    broadcast(m1,conn)
                    #prints the message and address of the user who just sent the message on the server terminal
                else:
                    remove(conn)
            except:
                continue

def broadcast(message,connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    conn, addr = server.accept()
    """
    Accepts a connection request and stores two parameters, conn which is a socket object for that user, and addr which contains
    the IP address of the client that just connected
    """
    list_of_clients.append(conn)
    print(addr[0] + " connected")
    start_new_thread(clientthread,(conn,addr))
    #creates and individual thread for every user that connects

conn.close()
server.close()
