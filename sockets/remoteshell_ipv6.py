import socketserver, argparse, socket
from subprocess import Popen, PIPE, STDOUT
import threading

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
        while True:
            data = self.request.recv(1024).strip()
            if len(data) == 0 or data == "exit":
                print(f"Cliente desconectado {self.client_address[0]}")
                exit(0)
            command = Popen([data], shell=True, stdout=PIPE, stderr=PIPE, text=True)
            stdout, stderr = command.communicate()
            if command.returncode == 0:
                ans = "OK \n"+ stdout
            else:
                ans = "ERROR \n"+ stderr
            self.request.send(ans.encode('ascii'))

def menu(dir, port):
    print(dir) #muestra el primer set 
    if dir[0] == socket.AF_INET: 
        if args.c == "p":
            server = ForkedTCPServer((HOST,port), MyServer)
            print(f"Lanzando servidor (Port= {port})")
        elif args.c == "t":
            server = ThreadTCPServer((HOST,port), MyServer)
            print(f"Lanzando servidor (Port= {port})")
    elif dir[0] == socket.AF_INET6:
        if args.c == "p":
            server = ForkedTCPServer_ipv6((HOST,port), MyServer)
            print(f"Lanzando servidor (Port= {port})")
        elif args.c == "t":
            server = ThreadTCPServer_ipv6((HOST,port), MyServer)
            print(f"Lanzando servidor (Port= {port})")
    server.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrip que simula una shell desde un servidor")
    parser.add_argument('-p', type=int, help="Ingresar puerto")
    parser.add_argument('-c', type=str, help="Ingrese 'p' para generar un proceso ó 't' para generar un hilo")
    args = parser.parse_args()
    HOST = ""
    PORT = args.p
    socketserver.TCPServer.allow_reuse_address = True
    directions = socket.getaddrinfo("localhost", args.p, socket.AF_UNSPEC, socket.SOCK_STREAM)
    workers = []
    for dir in directions:
        workers.append(threading.Thread(target=menu, args=(dir,args.p)))
    for worker in workers:
        worker.start()