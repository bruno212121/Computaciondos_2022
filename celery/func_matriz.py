"""
Realizar un programa en python que reciba por argumentos:

-f /ruta/al/archivo_matriz.txt

-c funcion_calculo
El programa deberá leer una matriz almacenada en el archivo de texto pasado por argumento -f, y 
deberá calcular la funcion_calculo para cada uno de sus elementos.

Para aumentar la performance, el programa utilizará un Celery, 
que recibirá mediante una cola de mensajes Redis, cada una de las tareas a ejecutar.

La funcion_calculo, modelada como tareas de Celery, podrá ser una de las siguientes:

raiz: calcula la raíz cuadrada del elemento.
pot: calcula la potencia del elemento elevado a si mismo.
log: calcula el logaritmo decimal de cada elemento.

"""
import os
import sys
import click, socket
from celery import Celery
from math import sqrt, log10, pow

app = Celery('func_matriz', broker='redis://localhost:6379', backend='redis://localhost:6379') 

@app.task
def pot(element):
    return pow(element, element)

@app.task
def raiz(element):
    return sqrt.int(element)

@app.task
def log(element):
    return log10.int(element)

@click.command()
@click.option('-f', '--file', 'file', help='Ruta al archivo de texto', required=True)
@click.option('-c', '--calc', 'calc', help='Funcion de calculo', required=True)

def main(file, calc):
    if not os.path.exists(file):
        print("El archivo no existe")
        sys.exit(1)
    if calc not in ['raiz', 'pot', 'log']:
        print("Función no válida")
        sys.exit(1)
    with open(file, 'r') as f:
        for line in f:
            for num in line.split():
                if calc == 'raiz':
                    result = app.send_task('func_matriz.raiz', args=[num])
                elif calc == 'pot':
                    result = app.send_task('func_matriz.pot', args=[num])
                elif calc == 'log':
                    result = app.send_task('func_matriz.log', args=[num])
                print(result.get())

if __name__=="__main__":
    main()
