# -*- coding: utf-8 -*-
# Counting sort 统计每种多少个直接改值太傻了
# 所以我们用 3 ways partition
class Solution(object):
    def sortColors(self, nums):
        for colFirst in range(len(nums)):
            if nums[colFirst] != 0:
                break
        for colLast in range(len(nums) - 1, -1, -1):
            if nums[colLast] != 2:
                break
        index = colFirst
        # 把中间混合区域中的0交换到左边（与colFirst交换），2交换到右边（与colLast交换）
        while index <= colLast:
            if nums[index] == 1:
                index += 1
            # colFirst stay at most left 1
            elif nums[index] == 0:
                nums[index], nums[colFirst] = nums[colFirst], nums[index]
                colFirst += 1
                index += 1
            # colLast stay at most right non 2
            elif nums[index] == 2:
                nums[index], nums[colLast] = nums[colLast], nums[index]
                colLast -= 1

        return nums

    def sortColors2(self, nums):
        # 两次partition
        for i in range(len(nums)):
            if nums[i] != 0:
                break

        for j in range(i, len(nums)):
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        for i in range(len(nums)):
            if nums[i] != 0 and nums[i] != 1:
                break

        for j in range(i, len(nums)):
            if nums[j] == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        return nums

test = Solution()
print test.sortColors([0, 1, 0, 2, 1, 2, 0])