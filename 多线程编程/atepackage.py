from atexit import register
def reg_1():
    print('I`m reg1 ')

def reg_2(name):
    print('I`m reg2 %s'%(name))

def reg_3(name1,name2,name3):
    print('I`m reg3 %s %s %s'%(name1,name2,name3))

register(reg_1)
register(reg_2,'reg2')
register(reg_3,'reg3','reg3','reg3')

@register
def reg_4():
    print('I`m reg4')

def main():
    print('All done')


if __name__ == '__main__':
    main()