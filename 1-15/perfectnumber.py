import math

num = 1

while True:
    accumlator = 0
    for i in range(1, num):
        if num % i == 0:
            accumlator += i
    if accumlator == num:
        print (num)
    num += 1