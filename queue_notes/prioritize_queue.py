# coding:utf-8
__author__ = 'lyb'
# Date:2018/8/19 20:06

import queue


class MyQueue(object):
    """定义自己的优先级队列"""
    def __init__(self, priority):
        self.priority = priority
        return

    def __lt__(self, other):
        return self.priority < other.priority
        # return self.priority > other.priority


q = queue.PriorityQueue()    # 按优先级顺序传入, 默认最小的优先, 更改__lt__ 的符号可以改变排序顺序
q.put(MyQueue(27))
q.put(MyQueue(18))
q.put(MyQueue(88))

while not q.empty():
    print(q.get().priority)

"""原生的"""
q1 = queue.PriorityQueue()
q1.put(55)
q1.put(22)
q1.put(98)
while not q1.empty():
    print(q1.get())

