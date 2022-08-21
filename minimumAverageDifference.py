class Solution(object):
    def minimumAverageDifference(self, nums):
        res = 0
        minVal = float('inf')
        preSum = []
        for n in nums:
            if len(preSum) == 0:
                preSum.append(n)
            else:
                preSum.append(preSum[-1] + n)
        for i in range(len(preSum) - 1):
            curr = abs(preSum[i] / (i + 1) - (preSum[-1] - preSum[i]) / (len(nums) - i - 1))
            if curr < minVal:
                res = i
                minVal = curr
        # partition at nums[-1]
        curr = abs(preSum[-1] / len(preSum))
        if curr < minVal:
            res = len(nums) - 1
        return res

test = Solution()
print test.minimumAverageDifference([2,5,3,9,5,3])
print test.minimumAverageDifference([0])
