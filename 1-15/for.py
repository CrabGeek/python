import random
import math
#This is about for and whileloop

the_list = [1,2,3,4,5]

for i in the_list:
    print (i)
"""
用for循环实现1~100之间的偶数求和

"""
acculmate = 0
for i in range(101):
    acculmate += i
print (acculmate)

"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
有7次机会

"""
number = int (input("Please entry a number between 1 to 10 "))
a = random.randint(1,11)
count = 7

while count > 0 :
    if a > number:
        number = int (input("Small, Try again "))
        count -= 1
    elif a < number:
        number = int (input("Big, Try again "))
        count -= 1
    else: 
        print ("You got it!")
        count = -1

"""
输出乘法口诀表(九九表)

"""
for i in range(1, 10):
    for j in range (1, 10):
        print("%d * %d = %d" %(i, j, i*j) )

#练习：------------------------------------------------------------------------------
"""
输入一个正整数判断它是不是素数

"""

num = int(input("please enter a number"))

end = int(math.sqrt(num)) + 1

is_prime = True

for i in range(2, end):
    if num % i == 0 or num < 1:
        is_prime = False
        break

if is_prime:
    print("This is prime number")
else:
    print("This is not prime")

"""
输入两个正整数计算最大公约数和最小公倍数

"""

num1 = int(input("Please enter first number"))
num2 = int(input("Please enter second number"))

lcm = num1 * num2

gcd = 0

while num1 != 0 and num2 != 0:
    if num1 > num2:
        num1 = num1 % num2
    else:
        num2 = num2 % num1

if num1 != 0:
    gcd = num1
else:
    gcd = num2

if gcd == 0:
    print("The gcd is 1 ")
    print("The lcm is %d" % (lcm))
else:
    lcm = lcm / gcd
    print("The gcd is %d" % (gcd)) 
    print("The lcm is %d" % lcm)


    



