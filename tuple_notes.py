# coding:utf-8
__author__ = 'lyb'
# Date:2018/8/10 10:58

list1 = ['a', 'd', 'g']
for i in list1:
    print(i)

tuple1 = ('f', 'u', 'i', 'h')
for i in tuple1:
    print(i)
# 元祖拆包
a1, a2, a3, a4 = tuple1
print(a1, a2, a3)

# 只想提取第一个的话
a1, *other = tuple1
print(a1, other)

# 一一对应， 多出的去掉， 前面的是键，后面的是值
print(dict(zip(list1, tuple1)))


"""
tuple 是不可变的，与 list 相比的优点：
性能优化，线程安全，可以作为 dict 的 key，拆包特性
dict 只有可以哈希的对象才能作为key， 就是不可改变的
"""

# dict

dict1 = {}
dict1[tuple1] = 'hello'
print(dict1)
"""
# TypeError: unhashable type: 'list'

dict1[list1] = 'hello'  
print(dict1)
"""