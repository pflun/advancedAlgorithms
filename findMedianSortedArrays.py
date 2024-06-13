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

    # naive solution, T is O(m + n) not O(log (m+n))
    def findMedianSortedArrays0(self, nums1, nums2):
        new_arr = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                new_arr.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                new_arr.append(nums2[j])
                j += 1
            else:
                new_arr.append(nums1[i])
                new_arr.append(nums2[j])
                i += 1
                j += 1
        if i < len(nums1):
            new_arr.extend(nums1[i:])
        if j < len(nums2):
            new_arr.extend(nums2[j:])
        if len(new_arr) % 2 != 0:
            return float(new_arr[len(new_arr) / 2])
        else:
            return float((new_arr[len(new_arr) / 2 - 1] + new_arr[len(new_arr) / 2])) / 2

test = Solution()
print test.findMedianSortedArrays0([1, 3], [2])
print test.findMedianSortedArrays0([1, 2], [3, 4])