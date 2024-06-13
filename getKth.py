class Solution(object):
    def getKth(self, lo, hi, k):
        cache = {1: 1}

        def helper(n):
            if n not in cache:
                if n % 2 == 0:
                    cache[n] = 1 + helper(n / 2)
                else:
                    cache[n] = 1 + helper(3 * n + 1)
            return cache[n]

        res = [i for i in range(lo, hi + 1)]
        # Or use heap
        res.sort(key=lambda x : helper(x))
        return res[k - 1]

test = Solution()
print test.getKth(12, 15, 2)
print test.getKth(7, 11, 4)