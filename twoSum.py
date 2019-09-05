# -*- coding: utf-8 -*-
# 使用哈希表 key为数组的值 value为数组的索引
# 然后遍历哈希表 对于每一个哈希表的key 都去找有没有存在target-key
# 存在的话 取出对应的值即可

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        # possible ans => index
        buff_dict = {}
        res = []
        for i in range(len(nums)):
            # print buff_dict
            if nums[i] in buff_dict:
                res.append([buff_dict[nums[i]], i])
                # return [buff_dict[nums[i]], i]
            else:
                # Throw possible ans into dict
                buff_dict[target - nums[i]] = i
        return res

    def twoSum2(self, nums, target):
        if len(nums) <= 1:
            return []

        res = []
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                res.append([dic[target - nums[i]], i])
            else:
                dic[nums[i]] = i

        return res

    def twoSumTwoPointers(self, nums, target):
        nums = sorted(nums)
        res = []
        low = 0
        high = len(nums) - 1
        while low < high:
            # this not able to handle duplicates
            if nums[low] + nums[high] == target:
                res.append([low, high])
                low += 1
                high -= 1
            elif nums[low] + nums[high] > target:
                high -= 1
            else:
                low += 1
        return res

test = Solution()
print test.twoSumTwoPointers([1, 2, 2, 4, 4, 6, 8, 8, 10], 10)