class Solution(object):
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