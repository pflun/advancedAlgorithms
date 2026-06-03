# -*- coding: utf-8 -*-
# stack：充当“记忆库”，保存外层和以前括号的得分。
# score：当前你所处的这一层级（这一对括号内）的得分
# 不要无脑往Stack里塞字符，当我从内层退回到外层时，我需要恢复什么信息？
# * 有时需要存字符：stack.append('(')（比如简单的验证有效括号）。
# * 有时需要存索引：stack.append(i)（比如求最长有效括号的长度）。
# * 有时需要存累加值/状态：stack.append(score)（就像你这道题，存的是历史得分）
# 所有这种类型的栈问题，都有一个标准模板：
# 1. 入栈 (Push - 深入下一层上下文)： 当遇到左括号 (，说明要开启新世界了。
# * 最佳操作： 把当前状态压入栈中保存，然后清空/重置当前状态变量，准备迎接新层级。
# 2. 出栈 (Pop - 返回上一层上下文)： 当遇到右括号 )，说明这一层结束了。
# * 最佳操作： 计算出当前层的最终结果，然后把栈顶的“老状态”弹出来，把新老结果合并 (Merge)
class Solution(object):
    def scoreOfParentheses(self, s):
        stack = []
        score = 0
        for c in s:
            if c == '(':
                stack.append(score)
                score = 0
            elif c == ')':
                if score == 0:
                    score = 1
                else:
                    score *= 2 # 如果score有分，必然是连续'))'
                score += stack.pop()
        return score

test = Solution()
print test.scoreOfParentheses("()")
print test.scoreOfParentheses("(())")
print test.scoreOfParentheses("()()")
print test.scoreOfParentheses("(()())")