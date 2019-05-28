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
        return v, self.dic

    def put(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:  # self.dic is full
                self.dic.popitem(last=False)
        self.dic[key] = value

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.put(3,3)
obj.put(1,1)
param_1 = obj.get(3)
param_2 = obj.get(3)
print param_1, param_2

print 'aabb'[:len('aabb')]
print 'awaglk'[0:4]
print max([1, 2, 4, 3])

if type([1, 2, 4, 3]) == list:
    print 'yes'
