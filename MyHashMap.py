# -*- coding: utf-8 -*-
# 二维数组，1000个空数组
class MyHashMap(object):

    def __init__(self):
        self.dict = [[] for _ in range(1000)]

    def hash(self, key):
        return key % 1000, key / 1000

    def put(self, key, value):
        hashkey, pos = self.hash(key)
        if len(self.dict[hashkey]) == 0:
            self.dict[hashkey] = [None for _ in range(1000)]
        self.dict[hashkey][pos] = value

    def get(self, key):
        hashkey, pos = self.hash(key)
        if len(self.dict[hashkey]) == 0:
            return -1
        return -1 if self.dict[hashkey][pos] is None else self.dict[hashkey][pos]

    def remove(self, key):
        hashkey, pos = self.hash(key)
        if len(self.dict[hashkey]) == 0:
            return
        self.dict[hashkey][pos] = None

test = MyHashMap()
test.put(20, 20)
print test.get(20)
test.remove(20)
print test.get(20)