class Solution(object):
    def maxValue(self, n, index, maxSum):
        lo = 1
        hi = maxSum
        while lo <= hi:
            mid = (lo + hi) / 2
            if self.helper(n, index ,maxSum, mid):
                lo = mid + 1
            else:
                hi = mid - 1
        return hi

    def helper(self, n, index, maxSum, m):
        left = index + 1
        right = n - index
        leftSum = 0
        rightSum = 0
        if left < m:
            leftSum = (m + (m - left + 1)) * left / 2
        else:
            leftSum = (m + 1) * m / 2
            leftSum += left - m
        if right < m:
            rightSum = (m + (m - right + 1)) * right / 2
        else:
            rightSum = (m + 1) * m / 2
            rightSum += right - m
        sumVal = leftSum + rightSum - m
        return True if sumVal <= maxSum else False

test = Solution()
print test.maxValue(4, 2, 6)
print test.maxValue(6, 1, 10)