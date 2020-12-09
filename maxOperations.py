class Solution(object):
    def maxOperations(self, nums, k):
        nums = sorted(nums)
        res = 0
        low = 0
        high = len(nums) - 1
        while low < high:
            if nums[low] + nums[high] == k:
                res += 1
                low += 1
                high -= 1
            elif nums[low] + nums[high] > k:
                high -= 1
            else:
                low += 1
        return res

test = Solution()
print test.maxOperations([1,2,3,4], 5)
print test.maxOperations([3,1,3,4,3], 6)