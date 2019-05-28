# -*- coding: utf-8 -*-
class Solution(object):
    def intersect(self, nums1, nums2):
        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    res.append(nums1[i])
                    break

        return res

    # What if the given array is already sorted? How would you optimize your algorithm?
    def intersectSorted(self, nums1, nums2):
        res = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res

    # Brutal force 找连续的一段
    def intersectArray(self, nums1, nums2):
        res = []
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                for m in range(len(nums2) - 1):
                    for n in range(m + 1, len(nums2)):
                        if nums1[i:j + 1] == nums2[m:n + 1]:
                            res.append(nums1[i:j + 1])
        return res

test = Solution()
print test.intersectSorted([1, 2, 3, 4], [2, 3, 4, 5])