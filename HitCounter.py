class HitCounter(object):
    def __init__(self):
        self.q = []

    def hit(self, timestamp):
        self.q.append(timestamp)

    def getHits(self, timestamp):
        # in past 5 min
        while self.q and timestamp - self.q[0] >= 300:
            self.q.pop(0)

        return len(self.q)

test = HitCounter()
test.hit(1)
test.hit(2)
test.hit(3)
test.hit(300)
test.hit(301)
print test.getHits(301)