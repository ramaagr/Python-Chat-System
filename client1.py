import socket
import select
import sys
from rearranger import *
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 4:
    print("Correct usage: script, IP address, port number,name")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
name=str(sys.argv[3])
server.connect((IP_address, Port))
while True:
    sockets_list = [sys.stdin, server]
    read_sockets = select.select([server], [], [], 1)[0]
    import msvcrt
    if msvcrt.kbhit():
        read_sockets.append(sys.stdin)
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(100000)
            m=message.decode()
            print(m)
        else:
            message = sys.stdin.readline()
            m1=renamer(name,message)
            m=m1.encode()
            server.send(m)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
