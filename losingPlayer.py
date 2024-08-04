class Solution(object):
    def losingPlayer(self, x, y):
        # only way to get 115 is one 75 + four 10
        # minimum pairs of 75 + 4 * 10
        res = min(x, y / 4)
        return 'Alice' if res % 2 != 0 else 'Bob'

test = Solution()
print test.losingPlayer(2, 7)
print test.losingPlayer(4, 11)
print test.losingPlayer(2, 1)