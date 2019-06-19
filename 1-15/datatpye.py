import math
#Numbers:
a = 1
b = 10

print (a)

#String:
s = "Hello"

print (s[1])
print (s[4])

#举例1:input输入以及格式化输出符号
a = int(input ('a = '))
b = int (input ('b = '))

print ("%d + %d = %d" % ( a, b, a + b))

#举例2:使用变量保存数据并进行算术运算
a = 321
b = 123
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) #整除
print(a % b)
print(a ** b) # a^b

#举例3: 强制转化
case = int(a)
print (case)

the_string = "10"
case1 = int(the_string)
print (case1)

the_string2 = "1.0"
case2 = float(the_string2)
print(case2)

case3 = 999
the_string3 = str(case3)
print(the_string3)

case4 = 78
the_string4 = chr(case4)
print(the_string4)

the_string5 = "a"
case5 = ord(the_string5)
print(case5)

#练习：------------------------------------------------------------
"""
将华氏温度转换为摄氏温度
F = 1.8C + 32
"""
f = float(input("please entry degree of temperature in f"))
c = (f - 32) / 1.8
print (c)

"""
输入半径计算圆的周长和面积

"""
r = float(input ("please the radiation of the cycle"))
area = math.pi * (r ** 2)
perimeter = 2 * math.pi * r

print ("The area is %.2f" % area) #保留两位小数
print ("The perimeter is %.2f" % perimeter)

"""
输入年份 如果是闰年输出True 否则输出False

"""
year = int(input("please input the year"))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print (is_leap)
