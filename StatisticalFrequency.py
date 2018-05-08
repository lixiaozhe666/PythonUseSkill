# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/08 8:47'
#统计频次
from random import randint
#1.找出列表中出现次数最多的三个元素
#方法1.1借助字典来完成统计工作并排序找出最多的前三个
aList = [randint(0,10) for x in range(0,20)]
print(aList)
bDict = dict.fromkeys(aList,0)#dict.fromkeys(alist,0),第一个参数为key值取值的集合，0表示value的默认值
for x in aList:
    if x in bDict.keys():
        bDict[x]+=1
bDict = sorted(bDict.items(),key=lambda x:x[1],reverse=True)[:3]
print(bDict)
#方法1.2 通过collection counter模块来统计并排序
from collections import Counter
tempList = [5, 7, 0, 9, 7, 8, 4, 2, 5, 9, 0, 9, 1, 2, 4, 3, 10, 3, 7, 6]
c = Counter(tempList)
print(c.most_common(3))

#2词频统计
import  re
text = '''
十年创作，五篇巨著，辰东用作品向我们证明了他的实力。厚重的文笔、深远的布局，还有对剧情起伏波折、前后呼应的掌控，辰东作品中的优点简直数不胜数，但最为人所称道的，无疑是他描写宏大场面时的惊人笔力。正是凭借着这一点，辰东在每一部作品中，都塑造出一个栩栩如生的、史诗般的玄幻世界，相信他的新作同样不会令我们失望！圣墟最新章节，《圣墟》全文免费在线阅读，作者辰东，《圣墟》内容简介：在破败中崛起在寂灭中复苏。 沧海成尘，雷电枯竭，那一缕幽雾又一次临近大地，世间的枷锁被打开了，一个全新的世界就此揭开神秘的一角
'''
text2='''
We are not born with courage, but neither are we born with fear. Maybe some of our fears are brought on by your own experiences, by what someone has told you, by what you’ve read in the papers. Some fears are valid, like walking alone in a bad part of town at two o’clock in the morning. But once you learn to avoid that situation, you won’t need to live in fear of it.
'''
wordList = re.split("\W+",text2)
cWord = Counter(wordList)
print(cWord.most_common(3))

