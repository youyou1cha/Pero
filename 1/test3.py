from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码
def write(q):
    print('Process to wirte:{}'.format(os.getpid()))
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


#  读数据进程执行代码
def read(q):
    print('Process to read:{}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建queue，并传递给各子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw,写入
    pw.start()
    # 启动子进程pr 读取
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程是while，无法join，直接杀死
    pr.terminate()
