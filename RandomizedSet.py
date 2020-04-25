# -*- coding: utf-8 -*-
import random

class RandomizedSet(object):
    def __init__(self):
        # 哈希表值指向数组index
        self.nums, self.pos = [], {}

    # val加到数组最后，哈希表指向数组最后一个index
    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    # 要删的index和最后的index值和指针都互换，然后pop掉。如果直接删要删除的index会把后面的index打乱
    def remove(self, val):
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx # self.nums move last val to target position, then pop; give index position to last
            print self.nums, self.pos
            self.nums.pop()
            self.pos.pop(val)
            return True
        return False
        # if val not in self.pos:
        #     return False
        # idx = self.pos[val]
        # self.nums[idx] = self.nums[-1]
        # self.pos[self.nums[-1]] = idx
        # self.pos.pop(val)
        # self.nums.pop()
        # return True

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]

test = RandomizedSet()
test.insert(1)
test.insert(2)
test.insert(5)
test.remove(2)
print test.nums, test.pos