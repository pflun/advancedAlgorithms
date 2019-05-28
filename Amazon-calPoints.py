# LC682 Baseball Game
class Solution(object):
    def calPoints(self, ops):
        if not ops or len(ops) == 0:
            return 0
        res = 0
        stack = []

        for op in ops:
            if op[0] == '-' or op.isdigit():
                stack.append(int(op))
                res += int(op)
            elif op == 'C':
                tmp = stack.pop()
                res -= tmp
            elif op == 'D':
                tmp = stack[-1] * 2
                stack.append(tmp)
                res += tmp
            elif op == '+':
                tmp = stack[-1] + stack[-2]
                stack.append(tmp)
                res += tmp

        return res

test = Solution()
print test.calPoints(["5","-2","4","C","D","9","+","+"])