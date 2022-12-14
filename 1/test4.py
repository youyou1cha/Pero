import threading
import time


def long_time_task(i):
    print('当前子线程:{} - 任务 {}'.format(threading.current_thread().name, i))
    time.sleep(2)
    print('结果:{}'.format(8 ** 20))


if __name__ == '__main__':
    start = time.time()
    print('这是主线程:{}'.format(threading.current_thread().name))
    thread_list = []
    for i in range(1,3):
        t = threading.Thread(target=long_time_task,args=(i,))
        thread_list.append(t)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()


    # t1 = threading.Thread(target=long_time_task, args=(1,))
    # t2 = threading.Thread(target=long_time_task, args=(2,))
    # t1.start()
    # t2.start()

    end = time.time()
    print('总用时间{}秒'.format((end - start)))
