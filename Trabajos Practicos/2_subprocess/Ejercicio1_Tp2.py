import subprocess as sp
import argparse

parser = argparse.ArgumentParser(description= "almacenar datos de salida de pantalla: ")

parser.add_argument("-c", "--command", type=str, help="Necesitas ingresar un comando")
parser.add_argument("-f", "--output_file", type=str, help="Necesitas la direccion del archivo salida")
parser.add_argument("-l", "--log_file", type=str, help="Archivos donde se almacenaran los comandos")
args = parser.parse_args()


output = open(args.output_file, "a")
logfile = open(args.log_file, "a")

process = sp.Popen([args.command], shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
stdout, stderr = process.communicate()
print(stdout)
print(stderr)

