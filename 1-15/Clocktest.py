from Clock import Clock

def main ():
    theClock = Clock(0,0,0)
    
    while True:
        theClock.show()
        theClock.run()


if __name__ == '__main__':
    main()
