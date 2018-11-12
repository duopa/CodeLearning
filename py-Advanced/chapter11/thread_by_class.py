import threading
import time
from chapter11 import var


def print_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")


def get_html():
    url_list = var.url_list
    while True:
        if len(url_list):
            url = url_list.pop()
            print("start to get html", url, print_time())
            time.sleep(2)
            print("end to get html", print_time())
            print()


def get_url():
    url_list = var.url_list
    while True:
        print("start to get url", print_time())
        time.sleep(4)
        for i in range(20):
            url_list.append('http://projectsedu.com/{id}'.format(id=i))
        print("end to get url", print_time())
        print()


class GetHtml(threading.Thread):

    def __init__(self):
        super().__init__()

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
    thread1 = GetHtml()
    thread1.start()
    thread2 = GetUrl('asiouhga')
    thread2.start()
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)

    # thread2.join()
    print(var.url_list)
    print("last time:{}".format(time.time() - start_time))






