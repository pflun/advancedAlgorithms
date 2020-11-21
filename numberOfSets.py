class Solution(object):
    def numberOfSets(self, n, k):

        def dp(n, k):
            if k >= n:
                return 0
            if k == 1:
                return n * (n - 1) / 2
            if k == n - 1:
                return 1
            res = 0
            for i in range(2, n - k + 2):
                res += (i - 1) * dp(n - i + 1, k - 1)
            return res
        return dp(n, k) % (10 ** 9 + 7)

test = Solution()
print test.numberOfSets(4, 2)