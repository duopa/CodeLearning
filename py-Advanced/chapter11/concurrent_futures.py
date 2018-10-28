from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED


# 线程池，为什么要线程池
# 主线程中可以获取某一个线程状态或者某一个任务的状态，以及返回值
# 当一个线程完成时我们主线程能立即知道
# futures可以让多线程和多进程编码接口一致

import time

def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=1)
# 通过submit函数提交执行的函数到线程池中，submit是立即返回
# task1 = executor.submit(get_html,(3))
# task2 = executor.submit(get_html,(2))

# 要获取已经成功的task的返回，谁先完成就处理谁
urls = [3,2,4]
all_task = [executor.submit(get_html,(url)) for url in urls]
wait(all_task, return_when=FIRST_COMPLETED)
print("main")
# for future in as_completed(all_task):
#     data = future.result()
#     print("get {} page success".format(data))

# 通过executor获取已经完成的task，按照url列表中的顺序返回
# for data in executor.map(get_html, urls):
#     print("get {} page".format(data))




# done方法，用于判定某个任务是否完成
# print(task1.done())
# print(task2.cancel())
time.sleep(3)
# print(task2.done())

# result 方法可以获取task的执行结果
# print(task1.result())