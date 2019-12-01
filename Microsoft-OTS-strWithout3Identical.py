# -*- coding: utf-8 -*-
# eedaaad => eedaad
# xxxtxxx => xxtxx
class Solution(object):
    def strWithout3Identical(self, S):
        res = S[0]
        cnt = 1
        for i in range(1, len(S)):
            if S[i] == S[i - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt < 3:
                res += S[i]
        return res

test = Solution()
print test.strWithout3Identical('eedaaad')
print test.strWithout3Identical('xxxtxxx')

# 给一个字符串S由a/b组成，可以任意替换a or b，求最小的action次数可以让整个字符串没有连续的三个相同字母
# https://leetcode.com/discuss/interview-question/398026/