class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        results = []
        Set1 = set(nums1)
        Set2 = set(nums2)
        for i in Set1:
            if i in Set2:
                results.append(i)
        return results


test = Solution()
print test.intersection([1, 2, 2, 1, 8], [8, 2, 2, 1, 3])
