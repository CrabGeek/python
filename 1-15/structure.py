import sys
import random

#LIst:
list1 = [1,2,3,4,5]

list1.append(200)
list1.insert(1,200)
list1 += [100,200]
print(list1)

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
print(list2)
list3 = sorted(list1, reverse=True)

print(list3)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)

print(sys.getsizeof(f))


#Turple
# 定义元组
t = ('骆昊', 38, True, '四川成都')
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])
# 遍历元组中的值
for member in t:
    print(member)
# 重新给元组赋值
#t[0] = '王大锤'  # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('王大锤', 20, True, '云南昆明')
print(t)
person = list(t)
print(person)
# 列表是可以修改它的元素的
person[0] = '李小龙'
person[1] = 25
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)


#集合：
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
set2 = set(range(1, 10))
print(set2)
set1.add(4)
set1.add(5)
set2.update([11, 12])
print(set1)
print(set2)
set2.discard(5)
print(set2)

# remove的元素如果不存在会引发KeyError
if 4 in set2:
    set2.remove(4)
print(set2)
# 遍历集合容器
for elem in set2:
    print(elem ** 2, end=' ')
print()
# 将元组转换成集合
set3 = set((1, 2, 3, 3, 2, 1))
print(set3.pop())
print(set3)
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))

#字典

scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
# 通过键可以获取字典中对应的值
print(scores['骆昊'])
print(scores['狄仁杰'])
# 对字典进行遍历(遍历的其实是键再通过键取对应的值)
for elem in scores:
    print('%s\t--->\t%d' % (elem, scores[elem]))
# 更新字典中的元素
scores['白元芳'] = 65
scores['诸葛王朗'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60))
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('骆昊', 100))
# 清空字典
scores.clear()
print(scores)

#练习：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

def create_code(code_len):
    string = ''
    while code_len > 0:
        choice = random.randint(0,1)
        if choice == 0: 
            charactor = str(random.randint(0, 10))
        else:
            charactor = chr(random.randint(65, 91))
        string += charactor

        code_len = code_len - 1
    return string

#练习2:设计一个函数返回给定文件名的后缀名。
def findFIleName (file):
    length = len(file)
    position = file.find('.')
    sub = file [position+1: length]
    return sub

#练习3:设计一个函数返回传入的列表中最大和第二大的元素的值。
def max2(theList):
    theNew = sorted(theList, reverse = True)
    return theNew[0], theNew[1]



if __name__ == '__main__':
    print(create_code(4))
    print(findFIleName("HEllo.c++"))
    print(max2([1,2,4,5,5,6,7,8]))
        

