from queue import Queue
import random, threading, time


# 生产者
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 5):
            print('{} is producing {} to the queue!'.format(self.name, i))
            self.queue.put(i)
            time.sleep(random.randrange(10) / 5)
        print("%s finished !" % self.name)


# 消费者
class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 5):
            var = self.queue.get()
            print("{} is consuming {} in the queue".format(self.name, var))
            time.sleep(random.randrange(10))
        print('{} finished '.format(self.name))


def main():
    queue = Queue()
    producer = Producer('Producer', queue)
    consumer = Consumer('consumer', queue)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    print('All threads finished')

if __name__ == '__main__':
    main()
