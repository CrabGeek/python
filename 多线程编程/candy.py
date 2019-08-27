#使用信号量来构建糖果机P156

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print("Refilling candy...")
    try:
        candytray.release()
    except:
        print('Full skipping')
    else:
        print('Ok')
    lock.release()

def buy():
    lock.acquire()
    print('Buying candy...')
    if candytray.acquire(False):
        print("Ok")
    else:
        print("Empty, Skipping")
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))


def main():
    print("Starting at:", ctime())
    nloops = randrange(3, 6)
    print('The CANDY MACHINE (full with %d bars) !' % MAX)
    Thread(target=consumer, args = (randrange(nloops, nloops + MAX + 2),)).start() #buyer
    Thread(target=producer, args=(nloops,)).start() #vndr

@register
def _atexit():
    print("ALl Done at:", ctime())

if __name__ == '__main__':
    main()