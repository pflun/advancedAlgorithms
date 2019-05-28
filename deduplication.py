# -*- coding: utf-8 -*-
# 给一个string，保证全是大小写英文字母，当出现同一个字母的一个大写挨着一个小写时候，消除掉这个pair。
# abBCcd -> return ad
# abBCcAd -> return d

class Solution(object):
    def deduplication(self, str):
        stack = []
        for s in str:
            # 一个字母的一个大写挨着一个小写， 或者stack[-1]大写，s小写；或者stack[-1]小写，s大写，分情况讨论
            if len(stack) != 0 and stack[-1].lower() == s.lower():
                stack.pop()
                continue
            else:
                stack.append(s)

        return ''.join(stack)

test = Solution()
print test.deduplication("abBCcAd")