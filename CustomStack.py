# -*- coding: utf-8 -*-
class CustomStack2(object):
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.stack = []
        self.inc = []  # 懒惰标记数组 (Lazy Increment array)

    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0)  # 新元素压入，初始增量标记为 0

    def pop(self):
        if not self.stack:
            return -1
        
        # 弹出栈顶元素及其绑定的增量标记
        val = self.stack.pop()
        increment = self.inc.pop()
        
        # 【核心操作】: 向下传递标记
        # 如果当前被弹出的元素包含增量，那么排在它下面的邻居一定也被包含在同一个 increment 范围内。
        # 因此，出栈时把这个增量继承给现在的栈顶元素。
        if self.inc:
            self.inc[-1] += increment
            
        return val + increment

    def increment(self, k, val):
        if self.stack:
            # 找到波及范围的最高点。
            # 如果 k 大于栈大小，就只标记当前的栈顶即可。
            idx = min(k - 1, len(self.stack) - 1)
            self.inc[idx] += val

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

print("--- CustomStack ---")
test = CustomStack(3)
test.push(1)
test.push(2)
print(test.pop())
test.push(2)
test.push(3)
test.push(4)
test.increment(5, 100)
test.increment(2, 100)
print(test.pop())
print(test.pop())
print(test.pop())
print(test.pop())

print("--- CustomStack2 (Lazy Increment) ---")
test2 = CustomStack2(3)
test2.push(1)
test2.push(2)
print(test2.pop())
test2.push(2)
test2.push(3)
test2.push(4)
test2.increment(5, 100)
test2.increment(2, 100)
print(test2.pop())
print(test2.pop())
print(test2.pop())
print(test2.pop())