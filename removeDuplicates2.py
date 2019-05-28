class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        counter = 0

        for i in nums:
            if counter < 2 or i > nums[counter - 2]:
                nums[counter] = i
                counter += 1
            print nums, counter, i
        return counter

test = Solution()
print test.removeDuplicates([1,1,1,2,2,3])