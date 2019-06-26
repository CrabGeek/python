from random import randint
import math


def roll_dice(n=2):
    """
    摇色子
    
    :param n: 色子的个数
    :return: n颗色子点数之和
    """
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))


# 在参数名前面的*表示args是一个可变参数
# 即在调用add函数时可以传入0个或多个参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))


# 练习：----------------------------------
'''
练习1：实现计算求最大公约数和最小公倍数的函数。
'''

def gcd (a, b):
    if a % b ==0 or b % a == 0:
        if a < b:
            return a 
        else:
            return b
    else:
        if a < b:
           return gcd (a, b % a )
        else:
           return gcd (a % b, b)
        
def lcm (a, b):
    return a * b / gcd(a, b)

print (gcd (18, 48))
print (lcm (7, 9))


'''
实现判断一个数是不是回文数的函数。
'''

def Sch_number (n):
    string = str(n)
    length = len(string)
    mid = int (length / 2)
    for i in range (0, mid):
        for j in range (mid + 1, length, -1):
            if i != j:
                return False

    return True

print (Sch_number(1221))

'''
练习3：实现判断一个数是不是素数的函数。
'''

def is_prime(n):
    end = int (math.sqrt(n))
    for i in range (2, end + 1):
        if n <= 1 or n % i == 0:
            return False
    return True 
        
print(is_prime(4))

'''
练习4：写一个程序判断输入的正整数是不是回文素数。
'''

if __name__ == '__main__':
    n = int(input("please enter a number"))
    if is_prime(n) and Sch_number(n):
        print(True)
    else:
        print(False)
        

