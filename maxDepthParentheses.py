class Solution(object):
    def maxDepth(self, s):
        res = 0
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
            if cnt < 0:
                cnt = 0
            res = max(res, cnt)
        return res