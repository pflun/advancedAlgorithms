class Solution(object):
    # Below is two pass solution, there's also a stack solution
    def minRemoveToMakeValid(self, s):
        cnt = 0
        i = 0
        while i < len(s):
            if s[i] == "(":
                cnt += 1
            elif s[i] == ")":
                cnt -= 1
            if cnt < 0:
                s = s[:i] + s[i + 1:]
                cnt += 1
            else:
                i += 1
        cnt = 0
        i = len(s) - 1
        while i >= 0:
            if s[i] == "(":
                cnt += 1
            elif s[i] == ")":
                cnt -= 1
            if cnt > 0:
                s = s[:i] + s[i + 1:]
                cnt -= 1
            i -= 1
        return s

# Remove Parentheses
test = Solution()
print test.minRemoveToMakeValid("())()(((")
print test.minRemoveToMakeValid("))((")
print test.minRemoveToMakeValid("lee(t(c)o)de)")