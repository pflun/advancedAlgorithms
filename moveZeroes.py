# -*- coding: utf-8 -*-
# Record the position of left 0, if != 0 then exchange, zero move to next, zero keep stay at left position of zeros

class Solution(object):
    def moveZeroes(self, nums):
        zero = 0  # records the position of "0"
        for i in xrange(len(nums)):
            # print i, zero, nums
            # two pointer, right pointer always move but left(zero) pointer stay at left-est zero, exchange when right != 0, left(zero) pointer move to next zero
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

        return nums

    # 把一个数组的偶数放前面，奇数放后面
    def BloombergmoveEvens(self, nums):
        even = 0  # records the position of even
        for i in xrange(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[even] = nums[even], nums[i]
                even += 1

        return nums

test = Solution()
print test.moveZeroes([2,0,1,3,0,12])
print test.BloombergmoveEvens([1,2,3,4,5,6,7,8])