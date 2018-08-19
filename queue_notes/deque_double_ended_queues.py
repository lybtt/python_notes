# coding:utf-8
__author__ = 'lyb'
# Date:2018/8/19 19:50

from collections import deque


d = deque(maxlen=3)   # maxlen 设置最大长度, 如果达到最大长度, 如果达到最大长度, 相对面的终端的值会被pop
d.append("b")
d.appendleft("a")
d.appendleft("c")
d.appendleft("d")
print(d)

d.pop()
d.popleft()
print(d)
