class Solution(object):
    def productExceptSelf(self, nums):
        if len(nums) <= 1:
            return False
        forth = [1]
        tmp = 1
        # forth traverse
        for i in range(1, len(nums)):
            tmp = tmp * nums[i - 1]
            forth.append(tmp)

        # back traverse, but I can calculate result in forth[] instead of another back array
        tmp = 1
        for i in range(len(nums) - 1, 0, -1):
            tmp = tmp * nums[i]
            forth[i - 1] = forth[i - 1] * tmp

        return forth

test = Solution()
print test.productExceptSelf([1,2,3,4])