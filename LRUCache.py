# -*- coding: utf-8 -*-
# https://aaronice.gitbooks.io/lintcode/content/data_structure/lru_cache.html
# https://www.youtube.com/watch?v=q1Njd3NWvlY
# A solution not using OrderedDict: https://discuss.leetcode.com/topic/14591/python-dict-double-linkedlist
# Heap, logn: https://discuss.leetcode.com/topic/45789/python-solution-using-heap-to-track-lru-item
# dict[key] => (value, time)    heap: (time, key)

from collections import OrderedDict
class LRUCache(object):
    def __init__(self, capacity):
        self.dic = OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v   # set key as the newest one
        return v

    def put(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:  # self.dic is full, last是最近的所以false就是最早进dict的
                self.dic.popitem(last=False)
        self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(3)
obj.put(1, 1)
obj.put(2, 2)
obj.put(3, 3)
print obj.get(1)
obj.put(4, 4)
print obj.get(2)