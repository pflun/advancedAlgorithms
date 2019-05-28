# -*- coding: utf-8 -*-
# Wiggle Sort II
# 先给数组排序，找到数组的中间的数，相当于把有序数组从中间分成两部分
# 然后从前半段的末尾取一个，在从后半的末尾去一个，这样保证了第一个数小于第二个数
# 然后从前半段取倒数第二个，从后半段取倒数第二个，这保证了第二个数大于第三个数，且第三个数小于第四个数
class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        low = 0
        high = len(nums) - 1
        mid = (low + high) / 2
        res = []
        low = mid + 1
        # [0,... <- mid, ... <- high]
        while high > mid:
            res.append(nums[low])
            res.append(nums[high])
            high -= 1
            low -= 1

        return res

test = Solution()
print test.wiggleSort([1, 5, 2, 1, 6, 4, 7])