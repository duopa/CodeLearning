# 多进程编程
# 耗CPU的操作，用于多进程编程，对于io操作来说，使用多线程编程，进程切换代价要高于线程

#1. 对于耗费cpu的操作，多进程优于多线程

from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
import time

def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)

# print(fib(36))

# if __name__ == "__main__":
#
#     with ProcessPoolExecutor(3) as executor:
#         all_task = [executor.submit(fib, (num)) for num in range(25,40)]
#         start_time = time.time()
#         for future in as_completed(all_task):
#             data = future.result()
#             print("exe result: {}".format(data))
#         print("last time is: {}".format(time.time()-start_time))


#2. 对于io操作来说，多线程由于多进程
def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == "__main__":

    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))
        print("last time is: {}".format(time.time()-start_time))





