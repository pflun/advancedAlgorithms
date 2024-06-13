# -*- coding: utf-8 -*-
# 只删两个数，那三个数里必然有一个留下和nums2配对
# 所以nums1剩下的数里面最小的必然配nums2最小的
# 所以nums1最小的三个数的差值必然有解
class Solution(object):
    def minimumAddedInteger(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        candidates = [nums2[0] - nums1[0], nums2[0] - nums1[1], nums2[0] - nums1[2]]
        candidates.sort()
        for i in candidates:
            tmp1 = []
            for n in nums1:
                tmp1.append(n + i)
            if self.sublist(tmp1, nums2):
                return i

    # if l2 is sublist of l1
    def sublist(self, l1, l2):
        dic1 = {}
        dic2 = {}
        for n in l1:
            dic1[n] = dic1.get(n, 0) + 1
        for n in l2:
            dic2[n] = dic2.get(n, 0) + 1
        # check if each freq in l2 is smaller or equal than l1
        for k, v in dic2.items():
            if k not in dic1 or dic1[k] < v:
                return False
        return True

test = Solution()
print test.minimumAddedInteger([4,20,16,12,8], [14,18,10])
print test.minimumAddedInteger([3,5,5,3], [7,7])
print test.minimumAddedInteger([9,9,1,1,1], [5,5,5])
print test.minimumAddedInteger([1,1,2,3], [4,5])
print test.minimumAddedInteger([1,1,2,3], [4,4])