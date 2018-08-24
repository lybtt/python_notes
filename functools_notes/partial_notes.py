# coding:utf-8
# author: 'lyb'
# Date:2018/8/24 20:07

# 不是很懂
import functools


def plus(a, b):
    return a + b


plus2 = functools.partial(plus, b=2)
for i in map(plus2, [1, 2, 3]):
    print(i)


