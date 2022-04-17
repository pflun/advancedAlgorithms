class Solution(object):
    def getXORSum(self, arr1, arr2):
        n1 = 0
        n2 = 0
        for a in arr1:
            n1 ^= a
        for a in arr2:
            n2 ^= a
        return n1 & n2

test = Solution()
print test.getXORSum([1,2,3], [6,5])
print test.getXORSum([12], [4])