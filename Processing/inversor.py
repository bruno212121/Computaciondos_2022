import os,argparse
import time, sys

parser = argparse.ArgumentParser(description="Archivo que genera procesos hijos como lineas tenga el archivo")

parser.add_argument("-f", help="Escribir el path")
args = parser.parse_args()

r, w = os.pipe()
r2, w2 = os.pipe()

file = open(args.f, 'r')

def child(x):
    for i in range(x):
        if os.fork() == 0:
            print("child")
            os._exit(0)

def f0():
    
    r2 = os.fdopen(r2)
    w.write(file)




if __name__=='__main__':
    lines = len(file.readlines())
    child(lines)
    for i in range(lines):
        os.wait()




