# -*- coding: utf-8 -*-
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