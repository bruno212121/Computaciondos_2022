import codecs
import queue
import threading as th, sys, os

def hilo(w, q):
    sys.stdin = open(0)
    line = sys.stdin.readline()
    os.write(w, line.encode('ascii'))
    line = q.get()
    q.task_done()
    print(f'H1 indent: {th.current_thread().ident} recupera la linea encriptada desde la cola de mensajes: ({line[:-1]})')


def hilo_uno(q, r):
    line = os.read(r, 100).decode()
    line = rot13(line)
    q.put(line)
    q.join()

def rot13(line):
    line_rot13 = codecs.encode(line, 'rot_13')
    return line_rot13

def main():
    w, r = os.pipe()
    q = queue.LifoQueue()

    hilo1 = th.Thread(target=hilo, args=(w, q))
    hilodos= th.Thread(target=hilo_uno, args=(q, r))

    hilo1.start()
    hilodos.start()

    hilo1.join()
    hilodos.join()

if __name__ == '__main__':
    main()

