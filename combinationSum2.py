# -*- coding: utf-8 -*-
# DFS with backtracking
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()

        return self.dfs(candidates, target, 0, [], [])

    def dfs(self, candidates, target, index, path, res):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return

        for i in xrange(index, len(candidates)):
            # if i != index and candidates[i] == candidates[i - 1]:
            #     continue

            self.dfs(candidates, target - candidates[i], i, path + [candidates[i]], res)
            if i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                continue

        return res


class Solution2(object):
    def combinationSumTwo(self, candidates, target):
        res = []
        import itertools
        for i in range(1, len(candidates) + 1):
            tmp = list(itertools.permutations(candidates, i))
            for candidate in tmp:
                if sum(candidate) == target:
                    if candidate not in res:
                        res.append(candidate)

        return res

# http://zxi.mytechroad.com/blog/searching/leetcode-40-combination-sum-ii/
class Solution3(object):
    def combinationSumTwo(self, candidates, target):
        self.res = []
        self.used = [False] * len(candidates)

        def dfs(nums, target, start, tmp):
            if target == 0:
                # shallow copy
                self.res.append(tmp[:])

            for i in range(start, len(nums)):
                if self.used[i]:
                    continue
                # 剪枝, otherwise exceed timing
                if nums[i] > target:
                    return

                self.used[i] = True
                tmp.append(nums[i])
                dfs(nums, target - nums[i], i, tmp)
                self.used[i] = False
                tmp.pop()

        dfs(sorted(candidates), target, 0, [])

        # Not an ideal solution, remove duplicates after LC46 permute.py
        res = []
        for elem in self.res:
            if elem not in res:
                res.append(elem)

        return res


test = Solution3()
print test.combinationSumTwo([10, 1, 2, 7, 6, 1, 5], 8)
