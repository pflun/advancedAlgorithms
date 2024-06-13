# -*- coding: utf-8 -*-
# Ignore the first solution, 题目的意思是出现多个*要从整个前面的substring里删除，而不是从上一个*到这个*之间内删除
# 那么就用min heap维护smallest idx need to be deleted
class Solution(object):
    def clearStars(self, s):
        res = []
        tmp = []
        idx = 0
        smallest = s[0]
        for i in range(len(s)):
            if s[i] == '*':
                if len(tmp) == 0:
                    idx = i + 1
                    if i + 1 < len(s):
                        smallest = s[i + 1]
                    continue
                else:
                    del tmp[idx - 1]
                    res.extend(tmp)
                    tmp = []
                    idx = 0
                    if i + 1 < len(s):
                        smallest = s[i + 1]
            else:
                tmp.append(s[i])
                if s[i] <= smallest:
                    idx = len(tmp)
                    smallest = s[i]
        if s[-1] != '*':
            res.extend(tmp)
        return ''.join(res)

test = Solution()
print test.clearStars("aaba*")
print test.clearStars("abc")
print test.clearStars("abc*abc*abc")
# 'k'
print test.clearStars("dk**")