# coding:utf-8
# author: 'lyb'
# Date:2018/8/24 20:26

from itertools import compress
from random import choice

# compress 接受两个集合对象, 只返回第一个对象里的值, 必须要第二个对象中值对应为True
numbers = range(1, 10)
boolean = [choice([True, False]) for _ in range(1, 10)]   # 1,0
print(boolean)
print(list(compress(numbers, boolean)))
