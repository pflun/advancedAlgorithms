class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        res = 0
        preSum = [0]
        for a in arr:
            preSum.append(preSum[-1] + a)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1):
                if (j - i) % 2 != 0:
                    res += preSum[j] - preSum[i]
        return res

test = Solution()
print test.sumOddLengthSubarrays([1,4,2,5,3])
print test.sumOddLengthSubarrays([1,2])
print test.sumOddLengthSubarrays([10,11,12])