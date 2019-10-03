import heapq
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        l = len(nums1) + len(nums2)
        if l % 2 != 0:
            return self.kth(nums1, nums2, l / 2 + 1)
        else:
            # convert to float then divide, e.g. float(5) / 2 = 2.5
            return float((self.kth(nums1, nums2, l / 2) + self.kth(nums1, nums2, l / 2 + 1))) / 2

    def kth(self, nums1, nums2, k):
        nums = nums1 + nums2
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]

test = Solution()
print test.findMedianSortedArrays([1, 3], [2])
print test.findMedianSortedArrays([1, 2], [3, 4])