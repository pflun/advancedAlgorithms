class Solution(object):
    # brutal force
    def longestArithSeqLength(self, A):
        self.res = 2

        def dfs(prev, length, diff):
            if prev == len(A) - 1:
                return
            for i in range(prev + 1, len(A)):
                if A[i] - A[prev] == diff:
                    length += 1
                    self.res = max(self.res, length)
                    dfs(i, length, A[i] - A[prev])
                    length -= 1

        for i in range(len(A) - 1):
            for j in range(i, len(A)):
                dfs(i, 1, A[j] - A[i])

        return self.res

test = Solution()
print test.longestArithSeqLength([9,4,7,2,10])