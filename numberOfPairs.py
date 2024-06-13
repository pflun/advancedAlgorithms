# -*- coding: utf-8 -*-
# 既然找divisible，就空间换时间，算出所有的整除因子(factor)和因子频率
# 那么num2 * k必然出现在预计算的因子中，出现的频率就是good pairs的次数
class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        res = 0
        # nums1's all factors and each freq
        dic = {}
        for n in nums1:
            factors = self.getAllFactor(n)
            for f in factors:
                dic[f] = dic.get(f, 0) + 1
        for n in nums2:
            # find if n * k in factors freq dic
            if n * k in dic:
                res += dic[n * k]
        return res

    def getAllFactor(self, n):
        res = set()
        for i in range(1, self.sqrt(n) + 1):
            if n % i == 0:
                res.add(i)
                res.add(n / i)
        return res

    def sqrt(self, x):
        if x == 0:
            return 0
        low = 1
        high = x
        while low != high - 1:
            mid = (high + low) / 2
            if mid * mid > x:
                high = mid
            elif mid * mid < x:
                low = mid
            if low == high - 1 or mid * mid == x:
                return mid
        return low

test = Solution()
print test.getAllFactor(12)
print test.getAllFactor(16)
print test.numberOfPairs([1,3,4], [1,3,4], 1)
print test.numberOfPairs([1,2,4,12], [2,4], 3)