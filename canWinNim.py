# Same to firstWillWin.py
class Solution(object):
    def canWinNim(self, n):
        if n == 0:
            return False
        elif n <= 3:
            return True

        res = [0] * (n + 1)
        res[0] = False
        res[1] = True
        res[2] = True
        res[3] = True

        for i in range(4, n + 1):
            res[i] = (not res[i - 1]) or (not res[i - 2]) or (not res[i - 3])

        return res[-1]

test = Solution()
print test.canWinNim(8)