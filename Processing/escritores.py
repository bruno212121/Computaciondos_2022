import argparse, os, string


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
    if not os.fork():

        if args.v:
            print("Proceso", os.getpid(), "Escribiendo letras: ", abc[letra])
        fd.write(abc[letra])

def padre():
    for i in range(args.n):
        hijos(i)


