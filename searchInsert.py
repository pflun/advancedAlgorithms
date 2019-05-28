class Solution(object):
    def searchInsert(self, nums, target):
        if target < nums[0]:
            return 0
        for i, val in enumerate(nums):
            if val == target:
                return i
            elif val > target:
                return i
        return i + 1


test = Solution()
print test.searchInsert([1,3,7,9], 10)