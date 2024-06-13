# -*- coding: utf-8 -*-
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# 在这个具体问题里，因为解是单调连续增加的序列 1,2..n，去重方法上可以稍微取巧一些：dfs里增加一个“前一个元素”的参数，每一层递归只考虑比上一个元素大的值。
class Solution:
    def combine(self, n, k):
        self.res = []
        self.used = [False] * (n + 1)

        def dfs(n, tmp, prev):
            if len(tmp) == k:
                # shallow copy
                self.res.append(tmp[:])

            for i in range(prev, n + 1):
                if self.used[i]:
                    continue
                self.used[i] = True
                tmp.append(i)
                dfs(n, tmp, i + 1)
                # backtracking:
                self.used[i] = False
                tmp.pop()

        dfs(n, [], 1)

        return self.res

test = Solution()
print test.combine(4, 2)