class Solution(object):
    def transpose(self, A):
        if len(A) == 0:
            return []
        res = [[None for _ in range(len(A))] for _ in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                res[j][i] = A[i][j]
        return res

test = Solution()
print test.transpose2([[1,2,3],[4,5,6],[7,8,9]])