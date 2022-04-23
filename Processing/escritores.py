import argparse, os, string
import time

parser = argparse.ArgumentParser(description="El programa genera <N> procesos hijos,cada proceso estará asociado a una letra del alfabeto")

parser.add_argument("-n", type=int, help="Ingrese un numero para generar procesos hijos.")
parser.add_argument("-r", type=int, help="Numero de veces que se repite la letra")
parser.add_argument("-f", type=str, help="Path del archivo a trabajar")
parser.add_argument("-v", action='store_true', help="Modo Verboso")

args = parser.parse_args()

abc = string.ascii_uppercase


def create_archivo(path):
    fd = open(path, "w+")
    return fd

fd = create_archivo(args.f)

def hijos(letra):
    if os.fork() == 0:
        if args.v:
            print("Proceso", os.getpid(), "Escribiendo letras: ", abc[letra])
        for i in range(args.r):
            fd.write(abc[letra])
        fd.flush()
        time.sleep(1)
        os._exit(0)


def padre():
    for i in range(args.n):
        hijos(i)
    for i in range(args.n):
        os.wait()
    fd = open(args.f, "r")
    lectura = fd.readlines()
    print(lectura)

padre()


