class Solution(object):
    def flipAndInvertImage(self, A):
        if len(A) == 0:
            return []

        def invert(a):
            return 1 if a == 0 else 0

        for x in range(len(A[0]) / 2):
            for y in range(len(A)):
                A[y][x], A[y][len(A[0]) - x - 1] = invert(A[y][len(A[0]) - x - 1]), invert(A[y][x])

        # odd columns
        if len(A[0]) % 2 != 0:
            for y in range(len(A)):
                A[y][len(A[0]) / 2] = invert(A[y][len(A[0]) / 2])

        return A

test = Solution()
print test.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])