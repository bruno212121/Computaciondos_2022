import argparse, multiprocessing as mp
from math import sqrt, log10
from functools import partial

parser = argparse.ArgumentParser(description="ejemplo parser")
parser.add_argument("-p", type=int, help="Cantidad de Procesos")
parser.add_argument("-f", help="Ruta de la matriz")
parser.add_argument("-c", help="funcion calculo (pot,raiz,log)")
args = parser.parse_args()

def read_matriz(path):
    file = open(path, 'r')
    matriz = file.readlines()
    matriz = [line.split(',') for line in matriz]
    return matriz

def calculator(fun, matriz):
    nueva_matriz = []
    for fila in matriz:
        nueva_fila = []
        for elemento in fila:
            elemento = calculate(fun, elemento)
            nueva_fila.append(elemento)
        nueva_matriz.append(nueva_fila)
    print(nueva_matriz)

def log(elemento):
    return log10(int(elemento))

def raiz(elemento):
    return sqrt(int(elemento))

def pot(elemento):
    return int(elemento)**int(elemento)

def calculate(fun, elemento):
    functions = {
        'pot': pot(elemento),
        'raiz': raiz(elemento),
        'log': log(elemento)
    }
    return functions[fun]

def main():
    pool = mp.Pool(args.p)
    results = pool.starmap(partial(calculator, args.c), [[read_matriz(args.f)]])

if __name__ == '__main__':
    main()