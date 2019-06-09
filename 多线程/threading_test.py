from threading import Thread
import queue
from time import sleep

q = queue.Queue()       # 任务队列
num_threads = 3         # 并发线程数
jobs = 10               # 任务数


# 处理单个任务
def do_something_using(arguments):
    print(arguments)


# 工作进程，负责不断从队列中取数据并处理
def working():
    while True:
        args = q.get()
        do_something_using(args)
        sleep(2)
        q.task_done()


for i in range(num_threads):
    t = Thread(target=working)
    t.setDaemon(True)
    t.start()

for i in range(jobs):
    q.put(i)

q.join()
