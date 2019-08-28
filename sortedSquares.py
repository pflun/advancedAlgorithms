class Solution(object):
    # brutal force
    def sortedSquares(self, A):
        res = []
        for a in A:
            a *= a
            res.append(a)
        return sorted(res)

    def sortedSquares2(self, A):
        l = 0
        r = len(A) - 1
        res = []
        while l <= r:
            if A[l] * A[l] > A[r] * A[r]:
                res.append(A[l] * A[l])
                l += 1
            else:
                res.append(A[r] * A[r])
                r -= 1
        return res[::-1]

test = Solution()
print test.sortedSquares2([-7,-3,2,3,11])