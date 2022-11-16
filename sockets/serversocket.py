import socketserver, argparse, subprocess, signal

class Thread(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class Process(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            data = self.request.recv(1024).strip()
            if len(data) == 0 or data == "exit":
                print(f"Cliente desconectado {self.client_address[0]}")
                server.shutdown()
                exit(0)
            command = subprocess.Popen([data], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = command.communicate()
            if command.returncode == 0:
                ans = "OK \n"+ stdout
            else:
                ans = "ERROR \n"+ stderr
            self.request.send(ans.encode('ascii'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrip que simula una shell desde un servidor")
    parser.add_argument('-p', type=int, help="Ingresar puerto")
    parser.add_argument('-c', type=str, help="Ingrese 'p' para generar un proceso ó 't' para generar un hilo")
    args = parser.parse_args()
    HOST, PORT = "", args.p
    socketserver.TCPServer.allow_reuse_address = True
    if args.c == "p":
        server = Process((HOST,PORT), MyTCPHandler)
        print(f"Lanzando servidor (Port= {PORT})")
        server.serve_forever()
    elif args.c == "t":
        server = Thread((HOST,PORT), MyTCPHandler)
        print(f"Lanzando servidor (Port= {PORT})")
        server.serve_forever()