from Person import Person 

def main():
    p1 = Person('王大锤', 12)
    p1.play()
    p1.age = 22
    p1.play()

    # AttributeError: 'Person' object has no attribute '_is_gay'
    person._is_gay = True


if __name__ == '__main__':
    main()