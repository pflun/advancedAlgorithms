class Solution(object):
    def balancedStringSplit(self, s):
        res = 0
        offset = 0
        for c in s:
            if c == 'L':
                offset += 1
            elif c == 'R':
                offset -= 1
            if offset == 0:
                res += 1
        return res

test = Solution()
print test.balancedStringSplit("RLLLLRRRLR")