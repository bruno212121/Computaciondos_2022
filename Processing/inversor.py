import os, argparse, time, sys

parser = argparse.ArgumentParser(description="Archivo que genera procesos hijos como lineas tenga el archivo")

parser.add_argument("-f", help="Escribir el path")
args = parser.parse_args()

r, w = os.pipe()
r2, w2 = os.pipe()

def leer_archivo():
    file = open(args.f, 'r')
    return file.readlines()

lineas_recibidas = []
def child(line):
    if not os.fork():
        os.write(w,line[::-1].encode('ascii'))
        os._exit(0)
    else:
        value = os.read(r, 100)
        lineas_recibidas.append(value.decode())


if __name__ == '__main__':
    lines = leer_archivo()
    r, w = os.pipe()
    for line in lines:
        child(line)
    for line in lines:
        os.wait()
    for line in lineas_recibidas:
        print(line)



