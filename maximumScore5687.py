class Solution(object):
    def maximumScore(self, nums, multipliers):
        self.memo = {}
        n = len(nums)
        m = len(multipliers)

        def dfs(l, r, i):
            if i == m:
                return 0
            if l in self.memo and r in self.memo[l]:
                return self.memo[l][r]
            res = max(nums[l] * multipliers[i] + dfs(l + 1, r, i + 1), nums[r] * multipliers[i] + dfs(l, r - 1, i + 1))
            if l not in self.memo:
                self.memo[l] = {r: res}
            else:
                self.memo[l] = {r: res}
            return res

        return dfs(0, n - 1, 0)

    # TLE
    def maximumScore2(self, nums, multipliers):
        self.cache = {}

        def dfs(i, j, k):
            if k == len(multipliers):
                return 0
            key = str(i) + '_' + str(j)
            if key in self.cache:
                return self.cache[key]
            l = nums[i] * multipliers[k] + dfs(i + 1, j, k + 1)
            r = nums[j] * multipliers[k] + dfs(i, j - 1, k + 1)
            self.cache[key] = max(l, r)
            return self.cache[key]

        return dfs(0, len(nums) - 1, 0)

test = Solution()
print test.maximumScore([1,2,3], [3,2,1])
print test.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6])