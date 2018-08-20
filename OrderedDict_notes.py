# coding:utf-8
__author__ = 'lyb'
# Date:2018/8/20 9:29


from collections import OrderedDict
import copy

# OrderedDict 排序字典
dict1 = OrderedDict()
dict1['A'] = 'a'
dict1['B'] = 'b'
dict1['C'] = 'c'
dict1['D'] = 'd'
for key, value in dict1.items():
    print(key, value)
print(dict1.keys())
dict2 = copy.deepcopy(dict1)
dict1.clear()  # 清空字典
print(dict2)

# 指定一个可迭代的对象, 把他的值作为字典的key, 生成一个字典

name = ('python', 'linux', 'mysql')
dict3 = OrderedDict.fromkeys(name, 20)
print(dict3)
