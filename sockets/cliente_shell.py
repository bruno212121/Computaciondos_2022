import socket, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-ht', help="Ingrese host servidor")
parser.add_argument('-p', type=int, help="Ingrese puerto servidor")

args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = args.ht
port = args.p

s.connect((host, port))

while True:
    print("Ingrese un comando")
    command = input('> ')
    if len(command) == 0 or command == "exit":
        print("Saliendo...")
        s.send(command.encode("ascii"))
        break
    else:
        s.send(command.encode("ascii"))
        recv = str(s.recv(1024).decode("ascii"))
        print(recv)