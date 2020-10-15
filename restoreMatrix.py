# greedy
# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/discuss/876845/JavaC%2B%2BPython-Easy-and-Concise-with-Prove
class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        res = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                tmp = min(rowSum[i], colSum[j])
                res[i][j] = tmp
                rowSum[i] -= tmp
                colSum[j] -= tmp
        return res

test = Solution()
print test.restoreMatrix([3,8], [4,7])
print test.restoreMatrix([5,7,10], [8,6,8])
print test.restoreMatrix([14,9], [6,9,8])
print test.restoreMatrix([1,0], [1])
print test.restoreMatrix([0], [0])