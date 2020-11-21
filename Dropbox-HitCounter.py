# Solution 1: below
# Solution 2: Circular array, save timestamp and counter in each cell
class HitCounter(object):
    def __init__(self):
        self.q = [] # timestamp
        self.dic = {} # timestamp => counter

    # improvement: poll those older than 5 min to avoid hit to many causing memory explode
    # hit can happen at the same time, still possible causing memory issue, use hashmap to store <timestamp, int counter>
    def hit(self, timestamp):
        if not self.q or timestamp != self.q[-1]:
            self.q.append(timestamp)
        self.dic[timestamp] = self.dic.get(timestamp, 0) + 1
        # clean up
        self.cleanUp(timestamp)

    def getHits(self, timestamp):
        # in past 5 min
        self.cleanUp(timestamp)
        res = 0
        for v in self.dic.values():
            res += v

        return res

    def cleanUp(self, timestamp):
        while self.q and timestamp - self.q[0] >= 300:
            outdated = self.q.pop(0)
            del self.dic[outdated]

test = HitCounter()
test.hit(1)
test.hit(2)
test.hit(3)
test.hit(300)
test.hit(300)
test.hit(301)
print test.getHits(301)