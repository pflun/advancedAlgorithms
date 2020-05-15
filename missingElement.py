# binary search: https://strstr.io/Leetcode1060-Missing-Element-in-Sorted-Array/
# but binary search doesn't improve time bc need to loop to find missings at each point
class Solution(object):
    def missingElement(self, nums, k):
        for i in range(1, len(nums)):
            k -= nums[i] - nums[i - 1] - 1
            if k == 0:
                return nums[i] - 1
            elif k < 0:
                return nums[i] + k - 1
        return nums[-1] + k

test = Solution()
print test.missingElement([4,7,9,10], 1)
print test.missingElement([4,7,9,10], 3)
print test.missingElement([1,2,4], 3)
print test.missingElement([4,7,9,10], 4)