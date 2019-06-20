import math

f1 = 1
f2 = 1

print(f1)
print(f2)

num = 0

while num < 100:
    fn = f1 + f2
    f1 = f2
    f2 = fn
    print(fn)
    num += 1