# similar to maxProfit3.py
class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        res = 0
        preSum = [nums[0]]
        for n in nums[1:]:
            preSum.append(n + preSum[-1])
        # first before second
        for i in range(len(nums) - firstLen):
            # get max first
            maxFirst = 0
            maxFirst = max(maxFirst, preSum[i + firstLen] - preSum[i])
            for j in range(i + firstLen, len(nums) - secondLen):
                # get max second
                maxSecond = 0
                maxSecond = max(maxSecond, preSum[j + secondLen] - preSum[j])
                res = max(res, maxFirst + maxSecond)
        # second before first
        for i in range(len(nums) - secondLen):
            maxSecond = 0
            maxSecond = max(maxSecond, preSum[i + secondLen] - preSum[i])
            for j in range(i + secondLen, len(nums) - firstLen):
                maxFirst = 0
                maxFirst = max(maxFirst, preSum[j + firstLen] - preSum[j])
                res = max(res, maxFirst + maxSecond)

        return res

test = Solution()
print test.maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1, 2)
print test.maxSumTwoNoOverlap([3,8,1,3,2,1,8,9,0], 3, 2)
print test.maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8], 4, 3)
print test.maxSumTwoNoOverlap([1,0,1], 1, 1)