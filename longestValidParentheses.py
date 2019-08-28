class Solution(object):
    def longestValidParentheses(self, s):
        dp, stack = [0] * (len(s) + 1), []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i + 1] = dp[p] + i - p + 1
        return max(dp)

    # https://www.youtube.com/watch?v=AqnGU4RjrxY
    def longestValidParentheses2(self, s):
        stack = []
        res = 0
        # record left idx
        start = -1
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    start = i
                else:
                    stack.pop()
                    if len(stack) == 0:
                        res = max(res, i - start)
                    # (())
                    else:
                        res = max(res, i - stack[0])
        return res

test = Solution()
print test.longestValidParentheses2(")()())")