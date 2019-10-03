# 678. Valid Parenthesis String
class Solution(object):
    def checkValidString(self, s):
        return self.dfs(s, 0)

    def dfs(self, s, idx):
        for i in range(idx, len(s)):
            if s[i] == '*':
                return self.dfs(s[:i] + '(' + s[i + 1:], i + 1) or self.dfs(s[:i] + ')' + s[i + 1:], i + 1) or self.dfs(s[:i] + s[i + 1:], i + 1)
            # exit check is leaf valid
            if i == len(s) - 1:
                return self.isValid(s)

    def isValid(self, s):
        stack = []
        for c in s:
            if c == ')':
                if len(stack) > 0:
                    curr = stack.pop()
                    if curr != '(':
                        return False
                else:
                    return False
            elif c == '(':
                stack.append(c)
        return True if len(stack) == 0 else False

test = Solution()
print test.checkValidString("(*)())")
print test.checkValidString("(*)()")