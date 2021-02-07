class Solution(object):
    def check(self, nums):
        minVal = min(nums)
        maxVal = max(nums)
        idx = 0
        max_idx = 0
        for i in range(len(nums)):
            if nums[i] == minVal:
                idx = i
                break
        if idx == 0:
            if nums == sorted(nums):
                return True
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] == maxVal:
                    max_idx = i
                    break
            nums_copy = nums[max_idx + 1:] + nums[:max_idx + 1]
            return True if nums_copy == sorted(nums) else False
        nums_copy = nums[idx:] + nums[:idx]
        return True if nums_copy == sorted(nums) else False

test = Solution()
# print test.check([3,4,5,1,2])
# print test.check([2,1,3,4])
# print test.check([1,2,3])
# print test.check([1,1,1])
# print test.check([2,1])
print test.check([6,10,6])
print test.check([7,9,1,1,1,3])