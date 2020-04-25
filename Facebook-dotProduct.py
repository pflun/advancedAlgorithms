# Given the following vectors (arbitrary numbers), design a more memory-efficient
#  representation of these vectors.
# A: [1, 1, 4, 4, 4, 4, 7, 7, 7, 7, 7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# B: [2, 2, 5, 5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
# Follow-up:
# With the vectors represented as suggested, write a function to calculate the
#  dot product of two vectors.
# Example:
# Input:
# A: [1, 1, 4, 4, 4, 4, 7, 7, 7, 7, 7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# B: [2, 2, 5, 5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
# Output: 291
# Explanation: 1 * 2 + 1 * 2 + 4 * 5 + ... + 2 * 3   Math Operation A*B = A1B1+A2B2+...+AnBn
# Additional information:
# The vectors are guaranteed to contain a large number of duplicate values,
#  similar to the example given above.
#  Follow-up:
# What if one of the vectors is very small?

class Solution(object):
    def compress_array(self, array):
        res = []
        start = 0
        while start < len(array):
            current = array[start]
            end = start
            count = 1
            while end + 1 < len(array) and array[end] == array[end + 1]:
                end += 1
                count += 1

            res.append([count, current])
            start = end + 1
        return res

    def dot_product(self, array1, array2):
        compress1 = self.compress_array(array1)
        compress2 = self.compress_array(array2)
        res = 0
        index1, index2 = 0, 0
        while index1 < len(compress1) and index2 < len(compress2):
            multiply = min(compress1[index1][0], compress2[index2][0])
            compress1[index1][0] -= multiply
            compress2[index2][0] -= multiply
            res += compress1[index1][1] * compress2[index2][1] * multiply

            index1 += 1 if compress1[index1][0] == 0 else 0
            index2 += 1 if compress2[index2][0] == 0 else 0
        return res