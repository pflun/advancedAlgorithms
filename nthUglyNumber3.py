# weekly contest 155, 2nd
import sys
class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        res = set()
        i = 1
        while i < sys.maxint:
            j = i
            while j < sys.maxint:
                k = i
                while k < sys.maxint:
                    res.add(k)
                    k *= c
                j *= b
            i *= a

        return sorted(list(res))[:n + 10]

test = Solution()
print test.nthUglyNumber(3, 2, 3, 5)