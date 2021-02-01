class Solution(object):
    def checkPartitioning(self, s):
        # pre calculate, if i to j is Palindrome
        dp = [[None for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                # 1 char
                if i == j:
                    dp[i][j] = True
                elif j == i + 1:
                    # 2 char
                    dp[i][j] = True if s[i] == s[j] else False
                else:
                    # 2+ char
                    dp[i][j] = True if dp[i + 1][j - 1] == True and s[i] == s[j] else False

        for i in range(len(s) - 1):
            for j in range(i + 1, len(s) - 1):
                if dp[0][i] and dp[i + 1][j] and dp[j + 1][-1]:
                    return True
        return False

test = Solution()
print test.checkPartitioning("abcbdd")
print test.checkPartitioning("bcbddxy")