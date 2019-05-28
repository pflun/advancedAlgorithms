# -*- coding: utf-8 -*-
# 排列和组合（permutation and combination）https://www.youtube.com/watch?v=zIY2BWdsbFs
# 典型的回溯
class Solution(object):
    def permuteUnique(self, nums):
        self.res = []
        self.used = [False] * len(nums)

        def dfs(nums, tmp):
            if len(tmp) == len(nums):
                # shallow copy
                self.res.append(tmp[:])

            for i in range(len(nums)):
                if self.used[i]:
                    continue
                # 如果curr和prev相等且prev已经用过，则跳过当前循环
                # 所以只有第一遍[1, 1, 2], [1, 2, 1]，第二遍跳过
                if i > 0 and nums[i] == nums[i - 1] and self.used[i - 1] == True:
                    continue
                # [1, 2] are used
                self.used[i] = True
                tmp.append(nums[i])
                dfs(nums, tmp)
                # after dfs([1, 2]) done, set used[2] to False for for loop [1, 3] && 2 not used yet
                self.used[i] = False
                tmp.pop()

        dfs(sorted(nums), [])

        # Not an ideal solution, remove duplicates after LC46 permute.py
        # res = []
        # for elem in self.res:
        #     if elem not in res:
        #         res.append(elem)

        return self.res

test = Solution()
print test.permuteUnique([2,1,1,2])