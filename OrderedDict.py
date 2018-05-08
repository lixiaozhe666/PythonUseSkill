# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/08 15:20'
from collections import OrderedDict
from random import randint
import time
d = OrderedDict()
start = time.time()
player = list('abcdefgh')
for i in range(8):
    input()
    end = time.time()

    p=player.pop(randint(0,7-i))
    d[p] = (i+1,end-start)
    print(p,d[p])

for k in d:
    print(k, d[k])