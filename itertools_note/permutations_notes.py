# coding:utf-8
# author: 'lyb'
# Date:2018/8/24 20:38

from itertools import permutations

# 获得列表所有的排列方式
colors = ['red', 'blue', 'black']
for random_colors in permutations(colors):
    print(random_colors)
