import random
class RandomizedCollection(object):
    def __init__(self):
        self.dic = {}
        self.data = []

    def insert(self, val):
        self.data.append(val)
        if val in self.dic:
            self.dic[val].append(len(self.data) - 1)
        else:
            self.dic[val] = [len(self.data) - 1]
        return True

    def remove(self, val):
        if val not in self.dic:
            return False
        else:
            lastVal = self.data.pop()
            currIdx = self.dic[val].pop()
            self.data[currIdx] = lastVal
            self.dic[lastVal].append(currIdx)
            return True

    def getRandom(self):
        return self.data[random.randint(0, len(self.data) - 1)]

test = RandomizedCollection()
print test.insert(1)
print test.insert(1)
print test.insert(2)
print test.getRandom()
print test.remove(1)
print test.getRandom()