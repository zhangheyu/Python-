# encoding: utf-8

from kazoo.client import KazooClient
import logging

zk = KazooClient(hosts='127.0.0.1:20153', retry_max_delay=60, logger=None)
zk.start()  # 与zookeeper连接
# makepath=True是递归创建,如果不加上中间那一段，就是建立一个空的节点
# zk.create('/China/GanSu/Pingliang/LingTai', b'this is my address', makepath=True)
# node = zk.get_children('/')  # 查看根节点有多少个子节点
# print(node)
# zk.stop()  # 与zookeeper断开

node = zk.get_children('/api/api_list')
print(node)
zk.stop()  # 与zookeeper断开
