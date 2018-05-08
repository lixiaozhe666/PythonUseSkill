# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/07 21:50'
from random import randint
#1.过滤掉所有负数
alist = [randint(-10,10) for x in range(10)]
positiveList = [x for x in alist if x>0]
positiveList2 = filter(lambda x:x>0,alist)
print(list(positiveList2))

#2.筛选出分数大于90的项
dDict = {x:randint(60,100)for x in 'abcdefghijk'}
GreatNinety = {k:v for k,v in dDict.items() if v>90}
print(GreatNinety)

#3.筛选出集合中能被3整除的数
sSet = set(randint(0,100) for x in range(100))
result = {x for x in sSet if x%3==0}
print(result)