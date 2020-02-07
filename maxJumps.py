# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=y5hRO6NvOHg
# 计划递归找最长满足条件的路径，Graph
class Solution(object):
    def maxJumps(self, arr, d):
        dp = [False for _ in range(len(arr))]

        def helper(i):
            # 已经递归求解过了
            if dp[i]:
                return dp[i]
            # base case，自己这一点的长度是1
            ans = 1
            # 向右递归
            j = i + 1
            while j < min(len(arr), i + d + 1) and arr[i] > arr[j]:
                ans = max(ans, helper(j) + 1)
                j += 1
            # 向左递归
            j = i - 1
            while j >= max(0, i - d) and arr[i] > arr[j]:
                ans = max(ans, helper(j) + 1)
                j -= 1
            # 找到最长，更新cache
            dp[i] = ans
            return ans

        res = 0
        # 对于每个节点找最长
        for i in range(len(arr)):
            res = max(res, helper(i))
        return res

test = Solution()
print test.maxJumps([6,4,14,6,8,13,9,7,10,6,12], 2)
print test.maxJumps([3,3,3,3,3], 3)
print test.maxJumps([7,6,5,4,3,2,1], 1)