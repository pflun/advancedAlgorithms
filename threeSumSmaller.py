# -*- coding: utf-8 -*-
class Solution(object):
    # two pointer, one from left (after i), the other one from most right
    # 跟 3 sum 一样，固定一点，从这点下一个开始两头往中间扫
    # 利用 sum < target 时，i 和 left 不动，介于 left 和 right (包括 right) 之间的所有元素 sum 也一定小于 target 的单调性。
    def threeSumSmaller(self, nums, target):
        nums.sort()
        length = len(nums) - 1
        res = []
        for i in range(length):
            j = i + 1
            k = length
            # two pointer
            while j < k:
                if nums[i] + nums[j] + nums[k] < target:
                    for l in range(j, k):
                        res.append([nums[i], nums[l], nums[k]])
                    j += 1
                else:
                    k -= 1

        return res

test = Solution()
print test.threeSumSmaller([-2, 0, 1, 3], 2)