class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.min_val = None

    def push(self, number):
        # write your code here
        if len(self.stack) == 0:
            self.min_val = number
        else:
            if number < self.min_val:
                self.min_val = number
        self.stack.append(number)

    def pop(self):
        # pop and return the top item in stack
        if len(self.stack) == 0:
            return False
        cur_min = self.stack.pop()
        # how to get the second min when pop happen to be the self.min_val? Set a second_min in __init__
        if cur_min == self.min_val:
            self.min_val = cur_min
        return cur_min

    def min(self):
        # return the minimum number in stack
        if len(self.stack) == 0:
            return False
        else:
            return self.min_val

class Min_Stack:
    def __init__(self):
        self.q = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin))

    # @return nothing
    def pop(self):
        self.q.pop()

    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]

    # @return an integer
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]

test = Min_Stack()
test.push(2)
test.push(1)
test.push(3)
node1, node2 = test.q.pop()

print node1, node2