# -*- coding: UTF-8 -*-

import threading
import time


def run(n):
    global num   # 把num变成全局变量
    time.sleep(1)  # 注意了sleep的时候是不占有cpu的，这个时候cpu直接把这个线程挂起了，此时cpu去干别的事情去了
    num += 1   # 所有的线程都做+1操作


num = 0   # 初始化num为0
t_obj = list()
for i in range(100):
    t = threading.Thread(target=run, args=("t-{0}".format(i),))
    t.start()
    t_obj.append(t)

for t in t_obj:
    t.join()


print("--------all thread has finished")
print("num:", num)   # 输出最后的num值是随机的不一定是100
# 这种情况只能在python2.x 中才会出现的，python3.x里面没有这种现象
