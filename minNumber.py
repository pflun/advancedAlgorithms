class Solution(object):
    def minNumber(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        d1 = nums1[0]
        d2 = nums2[0]
        for n1 in nums1:
            if n1 in nums2:
                return n1
        if d1 < d2:
            return d1 * 10 + d2
        elif d2 < d1:
            return d2 * 10 + d1