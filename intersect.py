# -*- coding: utf-8 -*-
# 用哈希表来建立nums1中字符和其出现个数之间的映射, 然后遍历nums2数组，
# 如果当前字符在哈希表中的个数大于0，则将此字符加入结果res中，然后哈希表的对应值自减1
class Solution(object):
    def intersectHashmap(self, nums1, nums2):
        res = []
        dic = {}
        for n in nums1:
            dic[n] = dic.get(n, 0) + 1
        for n in nums2:
            if n in dic and dic[n] > 0:
                res.append(n)
                dic[n] -= 1
        return res

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