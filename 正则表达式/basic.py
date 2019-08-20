import re


#使用 match(pattern, string, flags)
def matchFunction(parttern, target):
    m = re.match(parttern, target)
    if m is not None:
        print(m.group())
        if m.groups() is not () and m.group(1) is not None:
            print(m.groups())
    
    else:
        print("Can not find the pattern by using match function")


#使用 search(pattern, string, flags)
def searchFunction(parttern, target):
    m = re.search(parttern, target)
    if m is not None:
        print(m.group())

    else:
        print("Can not find the pattern by using search function")

#使用findall()和finditer()查找每一次出现的位置
#findall(pattern, string[,flaga]) and finditer(pattern, string[,flags])

def findallFunction(parttern, target):
    m = re.findall(parttern, target, re.I)
    if m is not None:
        print(m)

    else:
        print("Can not find the pattern by using search function")

def finditerFunction(parttern, target):
    m = re.finditer(parttern, target, re.I)
    if m is not None:
        print(next(m).groups())

    else:
        print("Can not find the pattern by using search function")
    

#使用sub函数来搜索替换
def subFunction(pattern,repl, target):

    print(re.sub(pattern, repl, target))

#使用split()函数 split(pattern, string, max)：
def splitFunction(pattern, target):
    print(re.split(pattern, target))



def main():
    matchFunction('foo','on the table foo ')
    searchFunction('foo','seafood on the table')

    #匹配多个字符串
    print("匹配多个字符串")
    bt = r'bat|bet|bit'
    matchFunction(bt, 'bit')
    matchFunction(bt, 'blt')
    matchFunction(bt, 'He bit me')
    searchFunction(bt, 'He bit me')

    #匹配单一字符
    print("匹配单一字符")
    anyend = '.end' 
    matchFunction(anyend, 'bend')
    matchFunction(anyend, 'end')
    matchFunction(anyend, '\nend')
    searchFunction(anyend, 'The end.')
    patt314 = '3.14'
    pi_patt = '3\.14'
    matchFunction(pi_patt, patt314)
    matchFunction(patt314, '3014')

    #创建字符集
    the_set = r'[cr][23][dp][o2]'
    matchFunction(the_set, 'c3p2')
    matchFunction(the_set, 'c2do')

    #重复，特殊字符以及分组
    patt = '\w+@(\w+\.)?\w+\.com'
    matchFunction(patt, 'nobody@xxx.com')
    matchFunction(patt, 'nrl172@163.com')
    
    patt1 = '\w\w\w-\d\d\d'
    matchFunction(patt1, 'ttt-012')
    
    patt2 = '(\w\w\w)-(\d\d\d)'
    matchFunction(patt2, 'xxx-234')

    #匹配字符串的起始和结尾以及单词边界
    patt3 = r'^The'
    searchFunction(patt3, 'The end')
    searchFunction(patt3, 'End, The')

    patt4 = r'\bthe'
    the_patt4 = '\bthe'
    searchFunction(patt4, 'bite the dog')
    print("Without 'r' key word ", the_patt4)

    searchFunction(patt4, 'bitethe dog')
    searchFunction(r'\Bthe', 'bitethe dog')

    #使用findall和finditer函数
    findallFunction('car', 'car')
    findallFunction('car', 'scary')
    findallFunction('car', 'carry the barcardi to the car')

    s = 'This and that'
    patt5 = r'(th\w+) and (th\w+)'

    
    findallFunction(patt5, s)
    finditerFunction(patt5, s)
    
    #使用sub(pattern, repl, string, count = 0)
    subFunction('X', 'Mr.Smith', 'attn: X\n\nDear, X\n')

    #使用split()分隔字符串
    splitFunction(';', 'str1;str2;str3')




if __name__ == '__main__':
    main()
