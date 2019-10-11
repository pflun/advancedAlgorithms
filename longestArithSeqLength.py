# DP: https://leetcode.com/problems/longest-arithmetic-sequence/discuss/274611/JavaC%2B%2BPython-DP
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

    # TLE
    def longestArithSeqLength2(self, A):
        res = 2
        for i in range(len(A)):
            first = A[i]
            for j in range(i + 1, len(A)):
                second = A[j]
                diff = first - second
                tmpLen = 2
                idx = j + 1
                while idx < len(A) and idx != -1:
                    try:
                        idx = A[idx:].index(second - diff)
                    except ValueError:
                        idx = -1
                    second = second - diff
                    if idx != -1:
                        tmpLen += 1
                        res = max(res, tmpLen)
        return res

test = Solution()
print test.longestArithSeqLength2([9,4,7,2,10])