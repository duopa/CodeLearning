from queue import Queue

import threading
import time
from chapter11 import var
def print_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")


def get_html(queue):
    while True:
        url = queue.get()
        print("start to get html", url, print_time())
        time.sleep(2)
        print("end to get html", print_time())
        print()

def get_url(queue):
        print("start to get url", print_time())
        time.sleep(4)
        for i in range(20):
            queue.put('http://projectsedu.com/{id}'.format(id=i))
        print("end to get url", print_time())
        print()


class GetHtml(threading.Thread):

    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("start to get html")
        time.sleep(2)
        print("end to get html")


class GetUrl(threading.Thread):

    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("start to get url")
        time.sleep(4)
        print("end to get url")


if __name__ == "__main__":
    start_time = time.time()
    # thread1 = GetHtml("get_html")
    # thread2 = GetUrl("get_url")
    detail_url_queue = Queue(maxsize=1000)

    thread1 = threading.Thread(target=get_url,args=(detail_url_queue,))
    thread1.start()
    for i in range(10):
        thread2 = threading.Thread(target=get_html,args=(detail_url_queue,))
        thread2.start()
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)

    detail_url_queue.task_done()
    detail_url_queue.join()

    # thread2.join()
    print(var.url_list)
    print("last time:{}".format(time.time() - start_time))






