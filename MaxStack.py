class MaxStack(objecct):
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
