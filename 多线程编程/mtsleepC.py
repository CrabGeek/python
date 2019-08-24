#使用threading 模块

import threading
from time import ctime,sleep

loops = [4, 2]


def loop(nloop, nsec):
    print("Start loop", nloop, "at:", ctime())
    sleep(nsec)
    print("loop", nloop, "done at:", ctime())


def main():
    threads = []
    nloops = range(len(loops))


    for i in nloops:
        t = threading.Thread(target= loop, args= (i, loops[i]))
        threads.append(t)

    for i in nloops:            #开始进程
        threads[i].start()

    for i in nloops:
        threads[i].join()   #等待所有进程结束

    print("All Done at:", ctime())


if __name__ == '__main__':
    main()

