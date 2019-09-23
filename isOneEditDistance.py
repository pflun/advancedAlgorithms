# -*- coding: utf-8 -*-
# 1. 两个字符串的长度之差大于1，直接返回False。
# 2. 两个字符串的长度之差等于1，长的那个字符串去掉一个字符，剩下的应该和短的字符串相同。
# 3. 两个字符串的长度之差等于0，两个字符串对应位置的字符只能有一处不同。
class Solution(object):
    def isOneEditDistance(self,s, t):
        if abs(len(s) - len(t)) >= 2:
            return False
        elif abs(len(s) - len(t)) == 1:
            if len(s) < len(t):
                s, t = t, s
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i + 1:] == t[i]
        else:
            cnt = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    if cnt != 0:
                        return False
                    else:
                        cnt += 1
            return True

test = Solution()
print test.isOneEditDistance("ab", "acb")