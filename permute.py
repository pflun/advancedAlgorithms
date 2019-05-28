# -*- coding: utf-8 -*-
# 排列和组合（permutation and combination）https://www.youtube.com/watch?v=zIY2BWdsbFs
# 典型的回溯
class Solution(object):
    def permute(self, nums):
        self.res = []

        def dfs(nums, tmp):
            # 递归到最底层curr list长度与输入长度相等, curr为其中一个解
            if len(tmp) == len(nums):
                # shallow copy
                self.res.append(tmp[:])

            for i in range(len(nums)):
                # if already exist, avoid [1, 1]
                if nums[i] in tmp:
                    continue
                # 1 append 2, ([1, 2]扔给下一个dfs处理), pop 2 then (下一个for) append 3 ([1, 3]扔给下一个dfs处理)
                tmp.append(nums[i])
                dfs(nums, tmp)
                # backtracking
                tmp.pop()

        dfs(nums, [])
        return self.res

    # O(n!)
    def permute2(self, nums):
        self.res = []
        self.used = [False] * len(nums)

        def dfs(nums, tmp):
            if len(tmp) == len(nums):
                # deep copy
                self.res.append(tmp[:])

            for i in range(len(nums)):
                if self.used[i]:
                    continue
                # [1, 2] are used
                self.used[i] = True
                tmp.append(nums[i])
                dfs(nums, tmp)
                # backtracking:
                # after dfs([1, 2]) done, set used[2] to False for for loop [1, 3] && 2 not used yet
                self.used[i] = False
                tmp.pop()

        dfs(nums, [])
        return self.res

test = Solution()
print test.permute([1,3,2])
print test.permute2([1,3,2])