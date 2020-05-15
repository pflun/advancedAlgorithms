# -*- coding: utf-8 -*-
# Contest时TLE了
# 解法2比较巧，还有一个解法3 PreSum：
# for(int i=0; i<=k; i++):
#     res = max(res, PreSum[i] + PostSum[k - 1]) 最终解出现在前i个和 + 后k-i个和上的某一点，所以预处理PreSum和PostSum
class Solution(object):
    # Problem Translation: Find the smallest subarray sum of length len(cardPoints) - k
    def maxScore2(self, cardPoints, k):
        l = 0
        r = len(cardPoints) - k
        res = sum(cardPoints[:r])
        tmp = res
        while r < len(cardPoints):
            tmp -= cardPoints[l]
            tmp += cardPoints[r]
            res = min(res, tmp)
            l += 1
            r += 1
        return sum(cardPoints) - res

    # TLE
    def maxScore(self, cardPoints, k):
        self.mem = [[False for _ in range(len(cardPoints))] for _ in range(len(cardPoints))]
        return self.helper(0, len(cardPoints) - 1, k, cardPoints)

    def helper(self, i, j, k, cardPoints):
        if k == 0:
            return 0
        if self.mem[i][j]:
            return self.mem[i][j]
        left = self.helper(i + 1, j, k - 1, cardPoints) + cardPoints[i]
        right = self.helper(i, j - 1, k - 1, cardPoints) + cardPoints[j]
        maxS = max(left, right)
        self.mem[i][j] = maxS
        return maxS

test = Solution()
print test.maxScore2([1,2,3,4,5,6,1], 3)
print test.maxScore2([2,2,2], 2)
print test.maxScore2([9,7,7,9,7,7,9], 7)
print test.maxScore2([1,1000,1], 1)
print test.maxScore2([1,79,80,1,1,1,200,1], 3)