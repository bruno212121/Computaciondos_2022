import socket, argparse
import concurrent.futures
from subprocess import Popen, PIPE, STDOUT

def shell(sock): 
    while True:
        data = sock.recv(1024)
        print(data) 
        if not data:
            break  
        proc = Popen(data, shell=True, stdout=PIPE, stderr=STDOUT)
        stdout_value = proc.communicate()[0]
        sock.send(stdout_value)
    sock.close()

def ProcHandler(sock, addr):
    print('Connected by', addr)
    shell(sock)

def THHandler(sock, addr):
    print('Connected by', addr)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(shell, sock)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Shell Remota')
    parser.add_argument('-c', '--concurrency', help='Tipo de concurrencia', required=True)
    args = parser.parse_args()
    if args.concurrency == 'process':
        with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
            s.bind(('', 50007))
            s.listen(1)
            while True:
                conn, addr = s.accept()
                with concurrent.futures.ProcessPoolExecutor() as executor:
                    executor.submit(ProcHandler, conn, addr)
    elif args.concurrency == 'thread':
        with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
            s.bind(('', 50007))
            s.listen(1)
            while True:
                conn, addr = s.accept()
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.submit(THHandler, conn, addr)
    else:
        print("Opción no válida")