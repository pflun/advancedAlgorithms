class Solution:
    # merge sort
    def mainSort(self, nums):
        nums = self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums, l, r):
        if l > r:
            return
        if l == r:
            return [nums[l]]
        mid = l + (r - l) / 2
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid + 1, r)
        return self.merge(left, right)

    def merge(self, l1, l2):
        res, i, j = [], 0, 0
        print l1, l2
        while i < len(l1) and j < len(l2):
            if l1[i] > l2[j]:
                res.append(l2[j])
                j += 1
            else:
                res.append(l1[i])
                i += 1
        res.extend(l1[i:] or l2[j:])
        return res

test = Solution()
print test.mainSort([2, 18, 9, 22, 17, 24, 8, 12, 27])