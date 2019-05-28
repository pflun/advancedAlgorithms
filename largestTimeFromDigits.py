# -*- coding: utf-8 -*-
# 应该用combination，我写成了permutation不允许重复，改
class Solution(object):
    def largestTimeFromDigits(self, A):
        if A == [0, 0, 0, 0]:
            return '00:00'

        self.max = 0
        self.used = [False] * len(A)

        def dfs(nums, tmp):
            # 递归到最底层curr list长度与输入长度相等, curr为其中一个解
            if len(tmp) == len(nums):
                # tmp加到4位时，求max
                self.max = max(int(''.join(str(i) for i in tmp)), self.max)

            for i in range(len(nums)):
                if self.used[i]:
                    continue
                self.used[i] = True
                # 1 append 2, ([1, 2]扔给下一个dfs处理), pop 2 then (下一个for) append 3 ([1, 3]扔给下一个dfs处理)
                tmp.append(nums[i])
                # 剪枝，前两位小于24或后两位小于60才允许继续递归
                if len(tmp) == 2 and int(''.join(str(i) for i in tmp)) < 24 or len(tmp) == 4 and int(''.join(str(i) for i in tmp[2:])) < 60 or len(tmp) == 1 or len(tmp) == 3:
                    dfs(nums, tmp)
                self.used[i] = False
                tmp.pop()

        dfs(A, [])
        return '' if self.max == 0 else str(self.max)[:2] + ':' + str(self.max)[2:]

test = Solution()
print test.largestTimeFromDigits([1, 2, 3, 3])
print test.largestTimeFromDigits([0,0,3,0])
