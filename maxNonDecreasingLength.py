class Solution(object):
    def maxNonDecreasingLength(self, nums1, nums2):
        dp1 = [1] * len(nums1)
        dp2 = [1] * len(nums1)
        for i in range(1, len(nums1)):
            if nums1[i] >= nums1[i - 1]:
                dp1[i] = dp1[i - 1] + 1
            if nums1[i] >= nums2[i - 1]:
                dp1[i] = max(dp1[i], dp2[i - 1] + 1)
            if nums2[i] >= nums2[i - 1]:
                dp2[i] = dp2[i - 1] + 1
            if nums2[i] >= nums1[i - 1]:
                dp2[i] = max(dp2[i], dp1[i - 1] + 1)
        return max(max(dp1), max(dp2))

test = Solution()
print test.maxNonDecreasingLength([2,3,1], [1,2,1])
print test.maxNonDecreasingLength([1,3,2,1], [2,2,3,4])
print test.maxNonDecreasingLength([1,1], [2,2])