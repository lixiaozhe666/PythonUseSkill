# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/07 22:14'
name,age,sex = 0,1,2 # name,age,sex =range(3)
student = ("xiaoli","18","male")
print(student[name])#等同于student[0]
print(student[age])#等同于student[1]
print(student[sex])#等同于student[2]

from collections import namedtuple
Student=namedtuple('Student',['name','age','sex'])
s=Student("xiaoli","18","male")
print(s.name)
print(s.age)
print(s.sex)
