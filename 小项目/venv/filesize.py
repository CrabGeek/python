import os
import sys

try:
    dic = sys.argv[1]

except IndexError:
    sys.exit("Must provide an argument")

dir_size = 0
fsizedir = {
    'B': 1,
    'KB': float(1)/ 1024,
    'MB': float(1)/ (1024 * 1024),
    'GB': float(1)/ (1024 * 1024 * 1024)

}

for (path, dirs, files) in os.walk(dic):
    for file in files:
        filename = os.path.join(path, file)
        dir_size += os.path.getsize(filename)


fsizeList = [str(round(fsizedir[key] * dir_size, 2)) + " " + key for key in fsizedir]

if dir_size == 0:
    print ("File is empty")
else:
    for u in sorted(fsizeList[::-1]):
        print("Fold size:", u)
