# -*- coding: utf-8 -*-
class Solution(object):
    def minimumNumbers(self, num, k):
        if num == 0:
            return 0
        if k == 0:
            if num % 10 == 0: # num = 100,000
                return 1
            else:
                return -1
        if num < k: # num = 8, k = 9
            return -1
        for i in range(1, 11): # i can be 10, num = 10, k = 1 should return 10
            if i * k > num: # num不够大，十位不够i个set来分了 num = 10, k = 8, i = 2时break
                return -1
            if num % 10 == (i * k) % 10: # num = X8, k = 9: 8 == 2 * 9 % 10
                return i
        return -1

test = Solution()
print test.minimumNumbers(10, 8)
print test.minimumNumbers(10, 1)