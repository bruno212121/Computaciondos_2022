import multiprocessing, codecs as mp , sys

def hijo_uno(conn, queue):
    sys.stdin = open(0)
    line = sys.stdin.readline()
    conn.send(line)
    line_queue = queue.get()

def hijo_dos(conn, queue):
    line = conn.recv()
