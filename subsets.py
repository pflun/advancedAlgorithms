# -*- coding: utf-8 -*-
# http://www.lintcode.com/en/problem/subsets/
# correct output but need to be careful about the order in output
# O(n * 2^n)
class Solution:
    def subsets2(self, nums):
        self.res = []

        def dfs(nums, tmp, used, idx):
            self.res.append(tmp[:])
            for i in range(idx, len(nums)):
                if nums[i] not in used:
                    tmp.append(nums[i])
                    used.add(nums[i])
                    dfs(nums, tmp, used, idx + 1)
                    tmp.pop()
                    used.remove(nums[i])

        dfs(nums, [], set(), 0)
        return self.res

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
print test.subsets2([1,2,3])