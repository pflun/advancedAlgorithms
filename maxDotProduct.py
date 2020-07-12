class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        dp = [[float('-inf') for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
        res = float('-inf')
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dp[i + 1][j + 1] = max(dp[i][j + 1], max(dp[i + 1][j], max(dp[i][j] + nums1[i] * nums2[j], max(dp[i][j], nums1[i] * nums2[j]))))
                res = max(res, dp[i + 1][j + 1])
        return res

test = Solution()
print test.maxDotProduct([2,1,-2,5], [3,0,-6])
print test.maxDotProduct([3,-2], [2,-6,7])
print test.maxDotProduct([-1,-1], [1,1])