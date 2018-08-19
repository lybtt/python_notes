# coding:utf-8
__author__ = 'lyb'
# Date:2018/8/19 19:25

import queue
from threading import Thread, current_thread


def get_my_queue(q):
    while True:
        print('the number is getted from {} :'.format(current_thread().getName()), q.get())
        q.task_done()  # Indicate that a formerly enqueued task is complete. 告诉队列操作已完成


q = queue.Queue()    # 线程安全的 queue 的数据结构, 多线程可以共享同一个 queue
num_threads = 5         # 线程的个数

for i in range(num_threads):
    worker = Thread(target=get_my_queue, args=(q,))
    worker.setDaemon(True)     # A boolean value indicating whether this thread is a daemon thread.
    worker.start()

for x in range(50):
    q.put(x)
q.join()     # Blocks until all items in the Queue have been gotten and processed. 直到队列为空
