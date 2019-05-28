class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        for num in nums:
            if num / 2 == 0:
                nums.append(nums.pop(num))
        return nums

test = Solution()
print test.partitionArray([1, 2, 3, 4])