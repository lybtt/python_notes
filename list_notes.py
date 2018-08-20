# coding:utf-8
import copy

__author__ = 'lyb'
# Date:2018/8/20 19:46

colors = ['red', 'blue', 'yellow', 'pink']
colors1 = copy.deepcopy(colors)
colors[1:2] = ['blue', 'black']   # 注意两者的区别
print(colors, colors1)
colors1[1] = ['blue', 'black']
print(colors1)
del colors1[1]   # 删除指定位置的元素
print(colors1)
colors2 = colors1 + colors
print(colors2)
print(colors2 * 3)
colors2.insert(0, 'hello')   # 在指定位置插入
print(colors2)
colors2.remove('hello')    # 移除指定元素
print(colors2)
print(colors2.pop(0))    # 指定位置
print(colors2.count('red'))     # 统计指定元素的个数
colors2.sort()          # 排序
print(colors2)
