class Solution(object):
    def minimumChairs(self, s):
        res = 0
        curr = 0
        for c in s:
            if c == 'E':
                curr += 1
            elif c == 'L':
                curr -= 1
            if curr < 0:
                curr = 0
            res = max(res, curr)
        return res