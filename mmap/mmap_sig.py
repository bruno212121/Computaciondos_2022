import os, sys, mmap, signal, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f",help="Path del archivo a escribir", required=True)
args = parser.parse_args()

segmento = mmap.mmap(-1, 1024) # Crea un segmento de memoria compartida anónima de 1024 bytes


def handler_dad(signum, frame):
    global continuar 
    if signum == signal.SIGUSR1:
        linea = segmento.readline()
        print("Linea recibida por el padre: ", linea)
        os.kill(pid_hijo2, signal.SIGUSR1)


def Capital_letter(signum, frame):
    segmento.seek(0)
    line = segmento.readline()
    file.write(line.decode().upper()) 
    file.flush() 

def end_child2(signum, frame):
    print("Hijo 2 terminado")
    os._exit(0)

def end_parent_child2(signum, frame):
    os.kill(pid_hijo2, signal.SIGUSR2)



def main():
    signal.signal(signal.SIGUSR1, handler_dad)
    signal.signal(signal.SIGUSR2, end_parent_child2)
    global child1
    child1 = os.fork()
    if child1 == 0:
        print("Ingrese linea: ")
        for line in sys.stdin:
            if line == "bye\n":
                os.kill(os.getppid(), signal.SIGUSR2)
                print("Hijo 1 terminando...")
                os._exit(0)
            segmento.seek(0)
            segmento.write(line.encode())
            segmento.seek(0)
            os.kill(os.getppid(), signal.SIGUSR1) 
    else:
        global pid_hijo2
        pid_hijo2 = os.fork()
        if pid_hijo2 == 0:
            signal.signal(signal.SIGUSR1, Capital_letter)
            signal.signal(signal.SIGUSR2, end_child2)

            while True:
                signal.pause()
        else:
            os.waitpid(child1, 0)
            os.waitpid(pid_hijo2, 0)
            print("Padre terminando...")

if __name__ == "__main__":
    file = open(args.f, 'a') 
    main()
