import time
import os

from multiprocessing import Process
def long_time_task():
    print('当前进程ID：{}'.format(os.getpid()))
    time.sleep(2)
    print('结果：{}'.format(8 ** 20))
def long_time_task_i(i):
    print('子进程:{} - 任务{}'.format(os.getpid(),i))
    time.sleep(2)
    print('结果：{}'.format(8 ** 20))

# if __name__ == '__main__':
#     print('当前母进程:{}'.format(os.getpid()))
#     start = time.time()
#     for i in range(2):
#         long_time_task()
#
#     end = time.time()
#     print('用时{}秒'.format(end - start))

if __name__ == '__main__':
    print('当前母进程:{}'.format(os.getpid()))
    start = time.time() 
    p1 = Process(target=long_time_task_i,args=(1,))
    p2 = Process(target=long_time_task_i,args=(2,))

    print('等待所以子进程完成')
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print('总共用时间{}'.format((end - start)))