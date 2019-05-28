# -*- coding: utf-8 -*-
# 理解错了，这么写不能cover nested，所以用stack
class Solution(object):
    def decodeString(self, s):
        res = ''
        i = 0
        while i < len(s):
            if s[i].isdigit():
                cnt = int(s[i])
                end = s[i + 1:].find(']')
                for _ in range(cnt):
                    res += s[i + 2:i + 1 + end]
                i = i + 1 + end
            elif s[i].isalpha():
                res += s[i]
            i += 1
        return res

test = Solution()
print test.decodeString("3[a2[c]]")