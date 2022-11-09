import socketserver, argparse, socket
import concurrent.futures
from subprocess import Popen, PIPE, STDOUT

#Server para IPv4
class ForkedTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class ThreadTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

#Server para IPv6
class ForkedTCPServer_ipv6(socketserver.ForkingMixIn, socketserver.TCPServer):
    address_family = socket.AF_INET6
    pass

class ThreadTCPServer_ipv6(socketserver.ThreadingMixIn, socketserver.TCPServer):
    address_family = socket.AF_INET6
    pass

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        while True:
            data = clientsocket.recv(1024)
            print("Address: %s " % str(addr))
            print("Recibido: "+data.decode("ascii"))
            msg = input('Enter message to send : ')
            clientsocket.send(msg.encode('ascii'))
            print("recibiendo", conn.send)
        conn.close()

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True