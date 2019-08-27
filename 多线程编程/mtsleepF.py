from atexit import register
from random import randrange
from threading import Thread, current_thread, Lock
from time import sleep, ctime

class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()
lock = Lock()
def loop(nsec):
    myname = current_thread().name
    lock.acquire()
    remaining.add(myname)
    print('[%s] Start %s' %(ctime(), myname))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print('[%s] Complete %s (%d secs)' %(ctime(), myname, nsec))
    print('(remaining: %s' %(remaining or None))
    lock.release()


def main():
    for pause in loops:
        Thread(target= loop, args=(pause, )).start()

@register
def _atexit():
    print('All Done at:', ctime())

if __name__ == '__main__':
    main()