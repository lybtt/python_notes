# coding:utf-8
# author: 'lyb'
# Date:2018/8/25 21:53


from collections import Counter


a = Counter(c=5, d=2)
b = Counter()
print(a)
print(b)
b.update("dddcc")
print(b)
print(a['c'])
print(a + b)
print(a - b)
print(a | b)
print(a & b)
print(a.most_common(1))     # 前n个最多的
