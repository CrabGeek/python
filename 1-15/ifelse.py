import math
"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

"""

x = float (input ("x = "))

if x > 1:
    sol = 3 * x - 5
elif x >= -1 and  x <= 1:
    sol = x + 2
else:
    sol = 5 * x + 3
print (sol)

#练习：--------------------------------------------------
"""
英制单位英寸和公制单位厘米互换

"""
length = float (input ("please entry the length that u want to tranfer "))
unit = str.lower(input ("Please entry the unit "))

if unit == "in" or unit == "inch":
    sol = length * 2.54
elif unit == "m" or unit == "meter":
    sol = length / 2.54
else:
    print("invald unit")

print ("The final solation is %f" % sol)

"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

"""
a = float (input("a = "))
b = float (input("b = "))
c = float (input("c = "))

if a + b > c or a + c > b or b + c > a:
    p = (a + b + c) / 2
    area = math.sqrt (p * (p - a) * (p - b) * (p - c)) 
    perimeter = p * 2
    print ("The perimeter is %f" % perimeter)
    print ("The area is %f" % area)

else:
    print("This is not 三角形")

    