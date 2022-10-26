import threading
import time

def long_time_task():
    print('子进程:{}'.format(threading.current_thread().name))
    time.sleep(2)
    print('结果:{}'.format(8 ** 20))

if __name__ == '__main__':
    start = time.time()
    print('主进程:{}'.format(threading.current_thread().name))
    for i in range(5):
        t = threading.Thread(target=long_time_task,args=())
        # t.setDaemon(True)
        t.daemon = 0
        t.start()

    end = time.time()
    print('总用时间{}秒'.format((end - start)))