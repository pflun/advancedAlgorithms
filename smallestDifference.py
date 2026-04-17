class Solution(object):
    def smallestDifference(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: int
        """
        a.sort()
        b.sort()
        i = j = 0
        res = float('inf')
        while i < len(a) and j < len(b):
            res = min(res, abs(a[i] - b[j]))
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
        return res

test = Solution()
print test.smallestDifference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8])