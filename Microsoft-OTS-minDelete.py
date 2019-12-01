# -*- coding: utf-8 -*-
# Min Deletions To Obtain String in Right Format, e.g. AAABBB
# BAAABAB, output:2 obtain AAABB by 删掉第一个B和最后一个A
# BBABAA output: 3 删掉所有A或者所有B
# we can partition the original string in half, deleting all B's in the left-side and all A's on the right side.
# A simple two-pass algorithm: by Keeping track of the number of 'B' on the left and the number of 'A' on the right,
class Solution(object):
    def minDelete(self, S):
        left = {'A': 0, 'B': 0}
        right = {}
        for c in S:
            right[c] = right.get(c, 0) + 1
        res = left['B'] + right['A']

        for c in S:
            left[c] += 1
            right[c] -= 1
            res = min(res, left['B'] + right['A'])
        return res

test = Solution()
print test.minDelete("BAAABAB")
print test.minDelete("BBABAA")
print test.minDelete("AABBBB")