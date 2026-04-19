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


from collections import defaultdict,OrderedDict
class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        # Maps key -> (value, frequency)
        self.key_map = {}
        # Maps frequency -> OrderedDict of keys
        self.freq_map = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key):
        if key not in self.key_map:
            return -1

        value, freq = self.key_map[key]
        self._update_freq(key, value, freq)
        return value

    def put(self, key, value):
        if self.capacity == 0:
            return

        # If key exists, just update its value and bump its frequency
        if key in self.key_map:
            _, freq = self.key_map[key]
            self._update_freq(key, value, freq)
            return

        # If capacity is full, evict the LFU (and LRU if tied) item
        if len(self.key_map) == self.capacity:
            # 1. Find the OrderedDict of the minimum frequency
            # 2. Pop the first item (Least Recently Used) from that OrderedDict
            evict_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.key_map[evict_key]

        # Insert the new key
        self.key_map[key] = (value, 1)
        self.freq_map[1][key] = None # Value in OrderedDict doesn't matter, just the key
        self.min_freq = 1

    def _update_freq(self, key, value, freq):
        """Helper method to promote a key to the next frequency bucket."""
        # Remove key from its current frequency bucket
        del self.freq_map[freq][key]

        # If we just emptied the bucket representing the min_freq, increment min_freq
        if freq == self.min_freq and not self.freq_map[freq]:
            self.min_freq += 1

        # Update mapping and add to the new frequency bucket
        self.key_map[key] = (value, freq + 1)
        self.freq_map[freq + 1][key] = None


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