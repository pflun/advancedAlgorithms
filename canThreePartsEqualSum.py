class Solution(object):
    def canThreePartsEqualSum(self, A):
        preSum = [A[0]]
        for a in A[1:]:
            preSum.append(preSum[-1] + a)
        for i in range(len(preSum) - 1):
            for j in range(i + 1, len(preSum)):
                first = preSum[i]
                second = preSum[j] - preSum[i]
                third = preSum[-1] - preSum[j]
                if first == second and second == third:
                    return True
        return False

test = Solution()
print test.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1])