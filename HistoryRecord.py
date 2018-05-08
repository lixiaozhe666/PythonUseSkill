# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/08 16:12'
from collections import deque#队列模块,可以把历史信息放到队列中 先进先出
import  pickle
q = deque([],5)#第一个参数为队列默认值，第二个为队列长度
for i in range(0,7):
    q.append(i)
print(q)
pickle.dump(q,open("history",'wb'))#保存python对象到本地文件 读写方式都为byte数据格式 wb
q2 = pickle.load(open("history",'rb'))#从文件载入对象带内存 读写方式都为byte数据格式 rb
print(q2)