import getopt
import sys

def main():
    try:
        (opt,args) = getopt.getopt(sys.argv[1:], 'm:n:o:', [])
    except getopt.GetoptError as err:
        print("ERROR", str(err))
        exit()
    if len(opt) !=3:
        print("The number of paramaters and arguments is incorrect.*")
        exit()
    else:
        print("ingrese las opciones:", opt)
    number1 = 0
    number2 = 0
    operator = ""

    for(op,arg) in (opt):
        if op == "-n":
            print("Number1: ",arg)
            number1 = int(arg)
        elif op == "-m":
            print("Number2: ",arg)
            number2 = int(arg)
        elif op == "-o":
            print("Operation: ", str(arg))
            operator = arg

    for(op,arg) in opt:
        if op == "-n":
            try:
                number1 = int(arg)
                number2 = int(arg)
            except ValueError:
                print("The numbers entered isn't integers, ")
                print("Number: ", arg)
                exit()
        if op == "-o":
            if arg.lower() not in["+","-","x","/"]:
                print("The entered operation is invalid. just use +,-,x or /")
                exit()
            operator = arg.lower()

    if op == "-o":
        if operator == "+":
            print(number1, "+", number2, "=", number1+number2)
        elif operator == "-":
            print(number1, "-", number2, "=", number1-number2)
        elif operator == "x":
            print(number1, "x", number2, "=", number1*number2)
        elif operator == "/":
            print(number1, "/", number2, "=", number1/number2)
            try:
                print(number1, "/", number2, "=", number1/number2)
            except zeroDivisionError as err:
                print("Sorry, you can´t divide 0.", err)
                sys.exit()
main()
