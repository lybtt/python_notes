# coding:utf-8
# author: 'lyb'
# Date:2018/8/24 20:23

from itertools import filterfalse


# 返回不满足条件的
numbers = range(1, 10)
print(list(filterfalse(lambda x: 2 < x < 7, numbers)))
