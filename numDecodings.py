class Solution(object):
    def numDecodings(self, s):
        if s == "" or s[0] == '0':
            return 0

        # init
        dp = [1, 1]
        for i in range(2, len(s) + 1):
            # [12,3] + [1,23]
            if 10 <= int(s[i - 2: i]) <= 26 and s[i - 1] != '0':
                dp.append(dp[i - 1] + dp[i - 2])
            # [1,20] or [1,10]
            elif int(s[i - 2: i]) == 10 or int(s[i - 2: i]) == 20:
                dp.append(dp[i - 2])
            # [13,1] or [10,1]
            elif s[i - 1] != '0':
                dp.append(dp[i - 1])
            # Cannot Decode
            else:
                return 0

        print dp
        return dp[len(s)]

test = Solution()
print test.numDecodings('12')