# 3228
# If it's 1,
# then increment the count ones,
# If it's 0,
# then it need at most ones operations,
# to move all ones 1s ending at this position.
class Solution(object):
    def maxOperations(self, s):
        res = 0
        ones = 0
        for i in range(len(s)):
            if s[i] == '1':
                ones += 1
            if i > 0 and s[i] < s[i - 1]:
                res += ones
        return res

test = Solution()
print test.maxOperations("1001101")
print test.maxOperations("00111")