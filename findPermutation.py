# -*- coding: utf-8 -*-
# 有bug
class Solution(object):
    def findPermutation(self, s):
        res = []
        for i in range(len(s) + 1):
            res.append(str(i + 1))

        for i in range(len(s)):
            if s[i] == 'D':
                idx = s[i:].find('I')
                res = self.reverseList(res, i, idx)

        return ''.join(res)

    def reverseList(self, res, i, idx):
        p1 = i
        p2 = idx + 2
        while p1 < p2:
            res[p1], res[p2] = res[p2], res[p1]
            p1 += 1
            p2 -= 1
        return res

test = Solution()
print test.findPermutation("ID")