import codecs
import multiprocessing as mp, sys


def hijo_uno(read, queue):
    sys.stdin = open(0)
    line = sys.stdin.readline()
    read.send(line)
    line_queue = queue.get()
    print(line_queue)


def hijo_dos(read, queue):
    line = read.recv()
    line_rot13 = codecs.encode(line, 'rot_13')
    queue.put(line_rot13)


def main():
    queue = mp.Queue()
    r, w = mp.Pipe()
    h1 = mp.Process(target=hijo_uno, args=(r, queue))
    h2 = mp.Process(target=hijo_dos, args=(w, queue))
    h1.start()
    h2.start()
    h1.join()
    h2.join()


if __name__ == '__main__':
    main()