# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/08 14:15'
#查找都拥有的key键
from random import randint,sample
from functools import reduce#python3 需要加入这一句，python2则不需要
d1 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
d2 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
d3 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
print(d1)
print(d2)
print(d3)
print(d1.keys() & d2.keys() & d3.keys())#python2.7使用print(d1.viewkeys() & d2.viewkeys() & d3.viewkeys())

#使用map(),reduce()函数进行查找相同key值

print(reduce(lambda x, y: x & y, map(dict.keys,[d1,d2,d3])))#key函数不能加（）
#reduce()累计运算函数，第一个参数为函数，第二个为一个迭代对象
#reduce(lambda x,y:x+y,[1,2,3]) 返回1+2+3 = 6
#map()函数 map() 会根据提供的函数对指定序列做映射。第二个参数列表的元素一次调用第一个函数参数