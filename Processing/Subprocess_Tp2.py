import argparse, subprocess as sp, datetime as dt

parser = argparse.ArgumentParser(description= "almacenar datos de salida de pantalla: ")

parser.add_argument("-c", "--command", type=str, help="Necesitas ingresar un comando")
parser.add_argument("-f", "--output_file", type=str, help="Necesitas la direccion del archivo salida")
parser.add_argument("-l", "--log_file", type=str, help="Archivos donde se almacenaran los comandos")
args = parser.parse_args()


args = parser.parse_args()

file_output = open(args.output_file, 'a')

process = sp.Popen([args.command], stdout=file_output, stderr=sp.PIPE, shell=True, universal_newlines=True)
error = process.communicate()[1]

if not error:
    fecha = dt.datetime.now()
    text = f"{fecha}: El comando {args.command} ejecutado correctamente\n"
    file_err = open(args.log_file, 'a')
    file_err.write(text)
    file_err.close()
else:
    fecha = dt.datetime.now()
    text = f"{fecha}: {error}"
    file_err = open(args.log_file, 'a')
    file_err.write(text)
    file_err.close()

file_output.writelines('\n')
file_output.close()
