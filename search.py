# -*- coding: utf-8 -*-
# search in rotate array
# https://www.youtube.com/watch?v=lWEIIFFflQY
class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            # 中线左边, nums[m] > nums[s] && nums[m] > nums[e]
            if nums[start] < nums[mid] and nums[end] < nums[mid]:
                # 画图就明白
                if nums[start] <= target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            # 中线右边, m < s && m < e
            elif nums[mid] < nums[end] and nums[start] > nums[mid]:
                if nums[mid] <= target and target <= nums[end]:
                    start = mid
                else:
                    end = mid

        return -1

test = Solution()
print test.search([4, 5, 6, 7, 0, 1, 2], 6)

