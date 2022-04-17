class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        idx = 0
        tmp = 0
        totalAbs = 0
        res = float('inf')
        for i in range(len(nums1)):
            if tmp < abs(nums1[i] - nums2[i]):
                idx = i
                tmp = abs(nums1[i] - nums2[i])
            totalAbs += abs(nums1[i] - nums2[i])

        before = abs(nums1[idx] - nums2[idx])
        for i in range(len(nums1)):
            after = abs(nums1[i] - nums2[idx])
            res = min(res, totalAbs - before + after)

        return min(res, totalAbs) % (10 ** 9 + 7)

test = Solution()
print test.minAbsoluteSumDiff([1,7,5], [2,3,5])
print test.minAbsoluteSumDiff([2,4,6,8,10], [2,4,6,8,10])
print test.minAbsoluteSumDiff([1,10,4,4,2,7], [9,3,5,1,7,4])