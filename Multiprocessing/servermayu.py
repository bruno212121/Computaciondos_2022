from string import whitespace
import sys
import socket
import multiprocessing

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = int(sys.argv[1])
host = "127.0.0.1"

serversocket.bind((host, port))                                  

serversocket.listen(5)
print("hola")
clientsocket, addr = serversocket.accept()

def child(conn):
    conn.send = str(input("escribir algo "))
    while True:
        data = clientsocket.recv(1024)
        print("Address: %s " % str(addr))
        print("Recibido: "+data.decode("ascii"))
        msg = input('Enter message to send : ')
        clientsocket.send(msg.encode('ascii'))
        print("recibiendo", conn.send)
    conn.close()
