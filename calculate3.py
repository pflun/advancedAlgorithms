# -*- coding: utf-8 -*-
# calculate2.py +-*/ 加入了括号 ()，括号的作用其实就是开启一个全新的、独立的计算环境。
# 遇到 ( 就进入递归，遇到 ) 就结束递归并返回当前括号内的计算结果。
# 为了让递归函数知道当前解析到了字符串的哪个位置，我们把字符串变成一个双端队列 (collections.deque)。
# 这样每次 popleft() 拿走一个字符，这个字符就真的消失了，全局共享这个进度，不需要传来传去传 index。
# 1. 把字符串变成 Queue：
# 主函数里直接 return self.helper(deque(s))。在 helper 里，我们用 while q: 替代原来的 while i < len(s):。
# 2. 简化数字的累加：
# 原来你用了一个内部的 while 循环去往后看是不是数字。现在因为我们是一个个从队列里弹字符，直接写 currNum = currNum * 10 + int(c) 就可以
# 3. 处理左括号 (：
# 当遇到 ( 时，说明要优先计算括号里的内容。直接调用递归 currNum = self.helper(q)。递归返回的结果，就相当于我们刚刚解析出了一个普通的数字。
# 4. 处理右括号 )：
# 右括号 ) 扮演了两个角色：
# * 第一，它和 + - * / 一样，是一个触发器。遇到它，说明前面的数字和符号该结算入栈了（所以判断条件变成了 if c in "+-*/)" or not q:）。
# * 第二，结算入栈后，它代表当前这个括号环境结束了，所以必须 break 跳出 while 循环，把当前 stack 里的数字求和并返回给上一层。
from collections import deque

class Solution(object):
    def calculate(self, s):
        # 把字符串转成队列，传给递归函数
        return self.helper(deque(s))
        
    def helper(self, q):
        res = 0
        stack = []
        currNum = 0
        sign = '+'  # 默认第一个数字是正数
        
        while q:
            c = q.popleft() # 弹出一个字符
            
            # 1. 如果是数字，累加
            if c.isdigit():
                currNum = currNum * 10 + int(c)
                
            # 2. 遇到左括号，进入递归！
            # 递归返回的值直接赋给 currNum，就好像我们刚读完一个数字一样
            if c == '(':
                currNum = self.helper(q)
                
            # 3. 遇到运算符、右括号、或者队列空了，触发计算逻辑
            if c in "+-*/)" or not q:
                if sign == '+':
                    stack.append(currNum)
                elif sign == '-':
                    stack.append(-currNum)
                elif sign == '*':
                    stack[-1] *= currNum
                elif sign == '/':
                    # 解决 Python 2 的负数除法向下取整的 bug (比如 -3/2 = -2)
                    # LeetCode 要求向零取整，所以用 int(float(a)/b)
                    stack[-1] = int(float(stack[-1]) / currNum)
                    
                # 更新符号，清空当前数字
                sign = c
                currNum = 0
                
            # 4. 遇到右括号，当前层级的计算结束，跳出循环
            if c == ')':
                break
                
        # 把栈里所有的数字加起来，就是当前层级（或者整个表达式）的结果
        for n in stack:
            res += n
            
        return res

# 测试代码
if __name__ == "__main__":
    test = Solution()
    print test.calculate("(2+3)*4")      # expect: 20
    print test.calculate(" 3+5 * 2")     # expect: 13
    print test.calculate("14-3/2")       # expect: 13
    print test.calculate("3+2*2")        # expect: 7
    print test.calculate("333+2*2")      # expect: 337
