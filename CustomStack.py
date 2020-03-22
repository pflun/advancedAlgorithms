class CustomStack(object):

    def __init__(self, maxSize):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        res = self.stack.pop()
        return res

    def increment(self, k, val):
        if k >= len(self.stack):
            for i in range(len(self.stack)):
                self.stack[i] += val
        else:
            for i in range(k):
                self.stack[i] += val

test = CustomStack(3)
test.push(1)
test.push(2)
print test.pop()
test.push(2)
test.push(3)
test.push(4)
test.increment(5, 100)
test.increment(2, 100)
print test.pop()
print test.pop()
print test.pop()
print test.pop()