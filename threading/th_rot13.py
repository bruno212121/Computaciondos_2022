import threading as th, sys, os, codecs

def read_sys(w):
    line = sys.stdin.readline()
    os.write(w, line.encode('ascii'))

def rot(r):
    line = os.read(r, 100).decode()
    line_rot13 = codecs.encode(line, 'rot_13')
    print(f'Texto cifrado: {line_rot13}')

if __name__ == '__main__':
    r, w = os.pipe()

    hilo = th.Thread(target=read_sys, args=(w,))
    hilodos= th.Thread(target=rot, args=(r,))

    hilo.start()
    hilodos.start()

    hilo.join()
    hilodos.join()

