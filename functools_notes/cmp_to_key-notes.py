# coding:utf-8
# author: 'lyb'
# Date:2018/8/24 20:14

# 不是很懂
from functools import cmp_to_key


def rev_diff(x, y):
    # return y - x
    return x - y


rev = cmp_to_key(rev_diff)

for i in sorted([5, 3, 2, 8], key=rev):
    print(i)


