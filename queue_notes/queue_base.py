# coding:utf-8
__author__ = 'lyb'
# Date:2018/8/19 19:56

import queue

q = queue.Queue(maxsize=3)
# Create a queue object with a given maximum size.If maxsize is <= 0, the queue size is infinite.
q.put(1)
q.put(2)
print(q.full())
q.put(3)
print(q.qsize())   # 获取 queue 的长度
print(q.empty())   # 判断是否为空
print(q.full())    # 判断是否满了
q.put(4, block=True, timeout=None)   # 如果队列已经满了可以使用 block 来阻塞, timeout 设置时间
q.get()
print(q.queue)

