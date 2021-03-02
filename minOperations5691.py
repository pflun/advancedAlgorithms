class Solution(object):
    def minOperations(self, nums1, nums2):
        res = 0
        maxPossible1 = 6 * len(nums1)
        minPossible1 = len(nums1)
        maxPossible2 = 6 * len(nums2)
        minPossible2 = len(nums2)
        if minPossible1 > maxPossible2 or minPossible2 > maxPossible1:
            return -1
        diff = sum(nums1) - sum(nums2)
        if diff == 0:
            return 0
        elif diff < 0:
            nums1, nums2 = nums2, nums1
        diff = abs(diff)
        dic1 = {}
        dic2 = {}
        for n in nums1:
            dic1[n] = dic1.get(n, 0) + 1
        for n in nums2:
            dic2[n] = dic2.get(n, 0) + 1
        for i in range(6, 0, -1):
            n1 = i
            n2 = 7 - i
            gain = i - 1
            if n1 not in dic1 and n2 not in dic2:
                continue
            cnt1 = dic1.get(n1, 0)
            cnt2 = dic2.get(n2, 0)
            if diff == gain * (cnt1 + cnt2):
                res += cnt1 + cnt2
                return res
            elif diff < gain * (cnt1 + cnt2):
                if diff % gain == 0:
                    res += diff / gain
                else:
                    res += diff / gain + 1
                return res
            else:
                diff -= gain * (cnt1 + cnt2)
                res += cnt1 + cnt2
        return res

test = Solution()
print test.minOperations([1,2,3,4,5,6], [1,1,2,2,2,2])
print test.minOperations([1,1,1,1,1,1,1], [6])
print test.minOperations([6,6], [1])
print test.minOperations([5,6,4,3,1,2], [6,3,3,1,4,5,3,4,1,3,4]) # 4
print test.minOperations([5,2,1,5,2,2,2,2,4,3,3,5], [1,4,5,5,6,3,1,3,3]) # 1