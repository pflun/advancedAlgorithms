# -*- coding: utf-8 -*-
# http://www.lintcode.com/en/problem/subsets/
# correct output but need to be careful about the order in output
# O(n * 2^n)
class Solution:
    def subsets(self, nums):
        self.res = []
        self.used = [False] * len(nums)

        def dfs(nums, index, tmp):
            self.res.append(tmp[:])

            for i in range(index, len(nums)):
                if self.used[i]:
                    continue
                # [1, 2] are used
                self.used[i] = True
                tmp.append(nums[i])
                dfs(nums, i, tmp)
                # after dfs([1, 2]) done, set used[2] to False for for loop [1, 3] && 2 not used yet
                self.used[i] = False
                tmp.pop()

        dfs(nums, 0, [])

        return self.res


test = Solution()
print test.subsets([1,2,3])