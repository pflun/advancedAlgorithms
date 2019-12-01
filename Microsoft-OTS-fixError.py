class Solution(object):
    def fixError(self, X, Y, A):
        N = len(A)
        result = -1
        nX = 0
        nY = 0
        for i in range(N):
            if A[i] == X:
                nX += 1
            elif A[i] == Y:
                nY += 1
            if nX != 0 and nY != 0 and nX == nY:
                result = i
        return result

test = Solution()
print test.fixError(7, 42, [6,42,11,7,1,42])
print test.fixError(7, 42, [42,42,11,7,1,42])
print test.fixError(7, 42, [6,42,11,7,1])
print test.fixError(7, 42, [])
print test.fixError(7, 42, [1,1,1,1])