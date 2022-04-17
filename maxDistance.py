class Solution(object):
    def maxDistance(self, nums1, nums2):
        res = 0
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                if i == j:
                    i += 1
                    j += 1
                elif i < j:
                    i += 1
            else:
                res = max(res, j - i)
                j += 1
        return res