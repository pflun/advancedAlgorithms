class SparseVector:
    # only store indices with values that are nonzero, index => value
    def __init__(self, nums):
        self.dic = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.dic[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        res = 0
        for k in vec.dic.keys():
            if k in self.dic:
                res += self.dic[k] * vec.dic[k]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)