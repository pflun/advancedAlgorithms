# -*- coding: utf-8 -*-
# https://www.cnblogs.com/grandyang/p/6258459.html
# 初始put(5), put(4), capacity = 2
# 然后我们的下一步操作是get(5)，下面是get需要做的步骤：
# 1. 如果m中不存在5，那么返回-1
# 2. 从freq中频率为1的list中将5删除
# 3. 将m中5对应的frequence值自增1
# 4. 将5保存到freq中频率为2的list的末尾
# 5. 在iter中保存5在freq中频率为2的list中的位置
# 6. 如果freq中频率为minFreq的list为空，minFreq自增1
# 7. 返回m中5对应的value值
# 下一步put(7)
# 1. 如果调用get(7)返回的结果不是-1，那么在将m中7对应的value更新为当前value，并返回
# 2. 如果此时m的大小大于了cap，即超过了cache的容量，则：
# 　　a）在m中移除minFreq对应的list的首元素的纪录，即移除4 -> {value4, 1}
# 　　b）在iter中清除4对应的纪录，即移除4 -> list.begin()
# 　　c）在freq中移除minFreq对应的list的首元素，即移除4
# 3. 在m中建立7的映射，即 7 -> {value7, 1}
# 4. 在freq中频率为1的list末尾加上7
# 5. 在iter中保存7在freq中频率为1的list中的位置
# 6. minFreq重置为1
class LFUCache2(object):

    def __init__(self, capacity):
        self.capacity = capacity
        # 保存当前最小频率
        self.minFreq = 0
        # 5 -> 1, 4 -> 1
        self.m = {}
        # 1 -> [5, 4]
        self.freq = {}
        # 4 -> list.begin() + 1
        # 5 -> list.begin()
        self.iter = {}

    def get(self, key):
        if not self.m[key]:
            return -1


    def put(self, key, value):
        return


# 再看了一遍好像下面写错了，具体看https://www.youtube.com/watch?v=MCTN3MM8vHA
from collections import OrderedDict
class LFUCache(object):
    def __init__(self, capacity):
        self.fq = OrderedDict()
        self.dic = {}
        self.remain = capacity

    def get(self, key):
        if key in self.dic:
            # 从fq拿出来再放进去，frequency ＋ 1
            fq = self.fq[key]
            self.fq.pop(key)
            self.fq[key] = fq + 1
            return self.dic[key]
        else:
            return -1

    def put(self, key, value):
        # 更新fq的顺序，fq ＋ 1，value加到dic
        if key in self.dic:
            self.dic[key] = value
            fq = self.fq[key]
            self.fq.pop(key)
            self.fq[key] = fq + 1
        else:
            # fq ＝ 1，remain －1
            if self.remain > 0:
                self.remain -= 1
                self.dic[key] = value
                self.fq[key] = 1
            # fq最后一个pop，同时把它从dic里pop
            else:
                lastKey, lastVal = self.fq.popitem(last=False)
                self.dic.pop(lastKey)
                self.dic[key] = value
                self.fq[key] = 1


# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(3)
obj.put(1, 1)
obj.put(2, 2)
obj.put(1, 1)
obj.put(2, 2)
# print obj.get(1)
obj.put(3, 3)
obj.put(4, 4)
obj.put(3, 3)
obj.put(3, 3)
# print obj.get(2)