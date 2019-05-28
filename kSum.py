# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=hLZedWtF2dc
class Solution(object):
    def kSum(self, nums, target, k):
        res = set()

        # 2 Sum
        if k == 2:
            if len(nums) <= 1:
                return []

            dic = {}
            for i in range(len(nums)):
                if target - nums[i] in dic:
                    res.add((target - nums[i], nums[i]))
                else:
                    dic[nums[i]] = i

        # 一层层往下剥， 降维，比如 4 Sum 降成直到 2 Sum
        else:
            left = 0
            while left < len(nums) - k + 1:
                for n in self.kSum(nums[left + 1:], target - nums[left], k - 1):
                    print n
                    res.add((nums[left],) + n)
                left += 1

        return res

test = Solution()
print test.kSum([1, 0, -1, 0, -2, 2], 0, 4)