# -*- coding: utf-8 -*-
class Solution(object):
    # two pointer, one from left (after i), the other one from most right
    # 跟 3 sum 一样，固定一点，从这点下一个开始两头往中间扫，根据diff更新res
    def threeSumClosest(self, nums, target):
        nums.sort()
        length = len(nums) - 1
        res = float('inf')
        for i in range(length):
            j = i + 1
            k = length
            # two pointer
            while j < k:
                if nums[i] + nums[j] + nums[k] == target:
                    return target
                elif nums[i] + nums[j] + nums[k] > 0:
                    if abs(nums[i] + nums[j] + nums[k] - target) < abs(res - target):
                        res = nums[i] + nums[j] + nums[k]
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    if abs(nums[i] + nums[j] + nums[k] - target) < abs(res - target):
                        res = nums[i] + nums[j] + nums[k]
                    j += 1

        return res

test = Solution()
print test.threeSumClosest([-1, 2, 1, -4], 1)