class MaxStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        if len(self.stack) == 0:
            self.stack.append([x, x])
        else:
            self.stack.append([x, max(x, self.stack[-1][1])])

    def pop(self):
        curr = self.stack.pop()
        return curr[0]

    def top(self):
        curr = self.stack[-1]
        return curr[0]

    def peekMax(self):
        curr = self.stack[-1]
        return curr[1]

    def popMax(self):
        arr = []
        maxVal = self.stack[-1][1]
        while self.stack and self.stack[-1][0] != maxVal:
            arr.append(self.stack.pop())
        curr = self.stack.pop()
        for a in arr[::-1]:
            self.push(a[0])
        return curr[0]

stack = MaxStack()
print stack.push(5)
print stack.push(1)
print stack.push(5)
print stack.top() # -> 5
print stack.popMax() # -> 5
print stack.top() # -> 1
print stack.peekMax() # -> 5
print stack.pop() # -> 1
print stack.top() # -> 5

print stack.push(2)
print stack.push(3)
print stack.push(4)
print stack.peekMax()
print stack.popMax()
print stack.peekMax()
print stack.pop()
print stack.top()