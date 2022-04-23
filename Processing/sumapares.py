import argparse, os

parser = argparse.ArgumentParser()

parser.add_argument("-n", type=int, help="Number")
parser.add_argument("-v", action='store_true', help="Verbose mode")
args = parser.parse_args()

for i in range(args.n):
    if os.fork() == 0:
        if args.v:
            print("Starting process", os.getpid())
        suma = sum([i for i in range(0, os.getpid()) if i % 2 == 0])
        print(f"{os.getpid()} - {os.getppid()}: {suma}")
        if args.v:
            print("Ending process", os.getpid())
        os._exit(0)

