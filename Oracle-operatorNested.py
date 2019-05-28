# -*- coding: utf-8 -*-
# 给个表达式如下，括号里面第一个是operator, 决定是加还是减。
# 然后跟着空格隔开的几个整数（或者是括号表达式）， 第一个数一直加（或减）后面所有的数，返回运算结果。
# 比如：
# 表达式 (+ 10 20) 返回 30
# (- (+ 2 4) (+ 5 5)) 返回 -4
# (+ 1 2 3) 返回 6
# (+ 1 2 4 (+ (+ (- 1 3) 3) 4 (+ 5 4 5 6)) 返回
class Solution(object):
    def operatorNested(self, string):
        stack = []
        for char in string:
            if char == ')':
                # Pop stack and get tmp to prepare level calculation
                stack, tmp = self.stackPop(stack, [])
                # get res for each level
                res = self.helper(tmp)
                # push res into stack for next calculation
                stack.append(res)
            else:
                stack.append(char)

        # for most outer level
        if stack:
            stack, tmp = self.stackPop(stack, [])
            res = self.helper(tmp)

        return res

    # Pop from stack from ')' to '('
    def stackPop(self, stack, tmp):
        while stack:
            if stack[-1] != '(':
                tmp.append(stack.pop())
            else:
                stack.pop()
                break

        return stack, tmp

    # calculate for each level
    def helper(self, tmp):
        operator = tmp.pop()
        # rm space
        tmp.pop()
        res = tmp.pop()

        for k in reversed(tmp):
            if k != ' ':
                # print res, operator, k
                # Tip: if operator is a string
                res = eval(res + operator + k)
                res = str(res)

        return res

test = Solution()
print test.operatorNested('(+ 1 2 4 (+ (+ (- 1 3) 3) 4 (+ 5 4 5 6))')