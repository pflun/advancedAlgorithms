# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=lAan667yWQ4
# 这个解法和two sum hashmap有异曲同工之妙，都是把两个for loop降成一个用hashmap
# 比如sum nums[0:2] % k得到一个余数 A，如果sum nums[0:5]也得到余数 A，就证明nums[2:5]刚好整除k
class Solution(object):
    def checkSubarraySum(self, nums, k):
        # remain => index
        dic = {}
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            print dic, tmp
            if k != 0:
                remain = tmp % k
            if remain in dic:
                # at least 2
                if i - dic[remain] > 1:
                    return True
            else:
                dic[remain] = i

        return False

    # Same as above
    def checkSubarraySum2(self, nums, k):
        if k == 0:
            return False
        preSum = []
        for n in nums:
            if len(preSum) == 0:
                preSum.append(n)
            else:
                preSum.append(preSum[-1] + n)
        dic = {}
        for i in range(len(preSum)):
            if preSum[i] % 6 in dic:
                if i - dic[preSum[i] % 6] > 1:
                    print i, dic[preSum[i] % 6], preSum, dic
                    return True
            else:
                dic[preSum[i] % 6] = i
        return False

test = Solution()
print test.checkSubarraySum([21, 7, 7, 4, 2], 6)
print test.checkSubarraySum2([23,2,4,6,7], 6)