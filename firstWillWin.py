# http://www.lintcode.com/en/problem/coins-in-a-line/
class Solution:
    def firstWillWin(self, n):
        if n == 0:
            return False
        elif n <= 2:
            return True

        res = [0] * (n + 1)
        res[0] = False
        res[1] = True
        res[2] = True

        for i in range(3, n + 1):
            res[i] = (not res[i - 1]) or (not res[i - 2])

        return res[-1]

test = Solution()
print test.firstWillWin(5)