class Solution(object):
    def transpose(self, A):

        if len(A) != len(A[0]):
            return False

        for y in range(len(A)):
            for x in range(len(A[0])):
                if x > y:
                    A[y][x], A[x][y] = A[x][y], A[y][x]

        return A

    # the other diagonal
    def transpose2(self, A):

        for y in range(len(A)):
            for x in range(len(A[0])):
                if x >= y and x + y <len(A) - 1:
                    print A[y][x]
                    A[y][x], A[x][y] = A[len(A) - x - 1][len(A) - y - 1], A[y][x]
                # if x > y and x + y <len(A) - 1:
                #     print A[y][x]
                #     A[y][x], A[x][y] = A[x][y], A[y][x]
        return A

test = Solution()
print test.transpose2([[1,2,3],[4,5,6],[7,8,9]])