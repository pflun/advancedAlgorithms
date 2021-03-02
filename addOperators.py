# -*- coding: utf-8 -*-
# 这第一个解法还可以用在calculator只有+/-/*上，把误加的减去，track上次一的乘就行（如果下一次不是乘，上次一的乘就是乘完加到res上）
class Solution(object):
    # num: remaining num string
    # temp: temporally string with operators added
    # cur: current result of "temp" string
    # last: last multiply-level number in "temp". if next operator is "multiply", "cur" and "last" will be updated
    def addOperators(self, num, target):
        res, self.target = [], target
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)  # this step put first number in the string
        return res

    def dfs(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num) + 1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
                self.dfs(num[i:], temp + "+" + val, cur + int(val), int(val), res)
                self.dfs(num[i:], temp + "-" + val, cur - int(val), -int(val), res)
                # 上面加减不解释了，下面乘是a + b * c => (a + b) - b + b * c，到b时默认+但是track上次加的b，到c时把上次误加的b减去，再加上b*c(这里也可能是误加取决于下次是+/*)，所以一直track这个可能误加的
                self.dfs(num[i:], temp + "*" + val, cur - last + last * int(val), last * int(val), res)

    def addOperators2(self, num, target):
        self.candidates = []
        self.res = []
        self.op = ['+', '-', '*']

        def dfs(num, tmp, idx):
            if idx == len(num):
                self.candidates.append(tmp[:])
                return

            for op in self.op:
                tmp.append(op)
                tmp.append(num[idx])
                dfs(num, tmp, idx + 1)
                tmp.pop()
                tmp.pop()

        dfs(num, [num[0]], 1)

        for c in self.candidates:
            if self.calc(c) == target:
                c = ''.join(c)
                self.res.append(c)
        return self.res

    def calc(self, arr):
        stack = [arr[0]]
        for i in range(1, len(arr), 2):
            prev = int(stack.pop())
            op = arr[i]
            next = int(arr[i + 1])
            if op == '*':
                prev = prev * next
                stack.append(prev)
            else:
                stack.append(prev)
                stack.append(op)
                stack.append(next)
        res = stack[0]
        for i in range(1, len(stack), 2):
            op = stack[i]
            next = stack[i + 1]
            if op == '+':
                res += next
            elif op == '-':
                res -= next
        return res

test = Solution()
print test.calc(['1', '+', '2', '*', '3', '*', '4', '-', '5'])
print test.addOperators2("123", 6)