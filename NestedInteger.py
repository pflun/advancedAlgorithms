class NestedInteger(object):
    def __init__(self, nestedList):
        self.idx = 0
        self.res = []
        for n in nestedList:
            if type(n) == int:
                self.res.append(n)
            elif type(n) == list:
                self.helper(n)

    def helper(self, nested):
        for n in nested:
            if type(n) == int:
                self.res.append(n)
            elif type(n) == list:
                self.helper(n)

    def next(self):
        if self.idx < len(self.res):
            nextVal = self.res[self.idx]
            self.idx += 1
            return nextVal
        else:
            return False

    def hasNext(self):
        return True if self.idx < len(self.res) else False

test = NestedInteger([1,2,[4,[6,8],[9,10],11]])
print test.next()
print test.next()
print test.hasNext()
print test.next()
print test.next()