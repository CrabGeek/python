#打开一个文件
f = open('NewFile.txt','w')
#写入
f.write("Python is a great language.\nYeah, its great")
#关闭文件
f.close()


#读取文件
r = open('NewFile.txt', 'r+')
#读取前十个字符

data = r.read(10)
print(data)

r.close()

#读取一行
l = open('NewFile.txt', 'r+')
data1 = l.readline()
data2 = l.readline()
print(data1)
print(data2)

l.close()

#读取多行
ls = open('NewFile.txt', 'r+')
data3 = ls.readlines()

print(data3)

ls.close()

#逐行读取
ll = open('NewFile.txt', 'r+')
for line in ll:
    print(line)
ll.close()

#逐行读取2去除换行符\n:
lbl = open('NewFile.txt', 'r+')
data4 = lbl.read().splitlines()
print(data4)

lbl.close()