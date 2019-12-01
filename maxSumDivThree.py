# -*- coding: utf-8 -*-
# 我写的这个解法有问题，看下面这个link
# https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/431057/Python-Math-Solution
class Solution(object):
    def maxSumDivThree(self, nums):
        res = 0
        one = []
        two = []
        for n in nums:
            if n % 3 == 0:
                res += n
            elif n % 3 == 1:
                one.append(n)
            elif n % 3 == 2:
                two.append(n)
        one.sort(reverse=True)
        two.sort(reverse=True)
        i = 0
        while i < len(one) and i < len(two):
            res += one[i] + two[i]
            i += 1
        if i == len(two) and i != len(one):
            i += 2
            while i < len(one):
                res += one[i] + one[i - 1] + one[i - 2]
                i += 3
        elif i == len(one) and i != len(two):
            i += 2
            while i < len(two):
                res += two[i] + two[i - 1] + two[i - 2]
                i += 3
        return res

test = Solution()
print test.maxSumDivThree([3,6,5,1,8])
print test.maxSumDivThree([4])
print test.maxSumDivThree([1,2,3,4,4])