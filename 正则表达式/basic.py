import re


#使用 match(pattern, string, flags)
def matchFunction(parttern, target):
    m = re.match(parttern, target)
    if m is not None:
        print(m.group())

    else:
        print("Can not find the pattern by using match function")


#使用 search(pattern, string, flags)
def searchFunction(parttern, target):
    m = re.search(parttern, target)
    if m is not None:
        print(m.group())

    else:
        print("Can not find the pattern by using search function")




def main():
    matchFunction('foo','on the table foo ')
    searchFunction('foo','seafood on the table')

    #匹配多个字符串

    print("匹配多个字符串")
    bt = 'bat|bet|bit'
    matchFunction(bt, 'bit')
    matchFunction(bt, 'blt')
    matchFunction(bt, 'He bit me')
    searchFunction(bt, 'He bit me')


if __name__ == '__main__':
    main()