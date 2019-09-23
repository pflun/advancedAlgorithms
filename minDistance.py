# https://www.youtube.com/watch?v=Q4i_rqON2-E
# bug
class Solution(object):
    def minDistance(self, word1, word2):
        l1 = len(word1)
        l2 = len(word2)
        self.dp = [[-1 for _ in range(l1 + 1)] for _ in range(l2 + 1)]

        def helper(word1, word2, l1, l2):
            if l1 == 0:
                return l2
            if l2 == 0:
                return l1
            if self.dp[l1][l2] >= 0:
                return self.dp[l1][l2]

            res = 0
            if word1[l1 - 1] == word2[l2 - 1]:
                res = helper(word1, word2, l1 - 1, l2 - 1)
            else:
                res = 1 + min(helper(word1, word2, l1 - 1, l2 - 1), min(helper(word1, word2, l1 - 1, l2), helper(word1, word2, l1, l2 - 1)))
            self.dp[l1][l2] = res
            return res

        return helper(word1, word2, l1, l2)

test = Solution()
print test.minDistance("horse", "ros")
