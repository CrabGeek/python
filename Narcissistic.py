import math

"""
水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、
自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），水仙花数是指一个 3 位数，
它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。

"""
num = int (input("Please enter a number"))
accumlator = 0

while num != 0:
    temp = num % 10
    accumlator += temp ** 3
    num = (num - temp) / 10

print(accumlator)
    
    

