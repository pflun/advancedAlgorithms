class Solution(object):
    def specialArray(self, nums):
        nums.sort()
        for i in range(1, nums[-1]):
            if self.helper(nums, i):
                return i
        return -1

    # find smallest element that larger than or equal target
    def helper(self, nums, x):
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] < x:
                low = mid + 1
            else:
                high = mid
        if nums[low] >= x and len(nums) - low == x:
            return True
        else:
            return False

test = Solution()
print test.specialArray([3,5])
print test.specialArray([0,0])
print test.specialArray([0,4,3,0,4])
print test.specialArray([3,6,7,7,0])
# this test case return -1, expect 100
print test.specialArray([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
                         100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
                         100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
                         100,100,100,100,100,100,100,100,100,100])