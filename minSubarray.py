class Solution(object):
    # TLE
    def minSubarray(self, nums, p):
        sumVal = sum(nums)
        if sumVal % p == 0:
            return 0
        preSum = [0]
        for n in nums:
            preSum.append(preSum[-1] + n)
        l = 1
        while l < len(nums):
            for i in range(len(nums) - l + 1):
                curr = preSum[i + l] - preSum[i]
                if (sumVal - curr) % p == 0:
                    return l
            l += 1

        return -1

test = Solution()
print test.minSubarray([3,1,4,2], 6)
print test.minSubarray([6,3,5,2], 9)
print test.minSubarray([1,2,3], 3)
print test.minSubarray([1,2,3], 7)
print test.minSubarray([1000000000,1000000000,1000000000], 3)