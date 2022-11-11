import os
import sys
import click

from celery_config import pot, log, raiz

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
            # print(line)
            for num in line.split(","): 
                print(f" numero de la matriz :{num}")
                if calc == 'raiz':
                    resultado = raiz.delay(int(num))
                elif calc == 'pot':
                    resultado = pot.delay(int(num))
                elif calc == 'log':
                    resultado = log.delay(int(num))
                print(resultado)
                res = AsyncResult(result.id)
                print(res.get())

if __name__=="__main__":
    main()
