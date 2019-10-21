# Suppose we have very large sparse vectors (most of the elements in vector are zeros)
#
# Find a data structure to store them
# Compute the Dot Product.
# Follow-up:
# What if one of the vectors is very small?

class Solution(object):
    def dotProduct(self, arr1, arr2):
        # two pointer
        res = 0
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i][0] == arr2[j][0]:
                res += arr1[i][1] * arr2[j][1]
            elif arr1[i][0] < arr2[j][0]:
                i += 1
            else:
                j += 1
        return res