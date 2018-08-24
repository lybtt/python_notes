# coding:utf-8
# author: 'lyb'
# Date:2018/8/24 20:21

from itertools import chain

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]
print(list(chain(letters, numbers)))
