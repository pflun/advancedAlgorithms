# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=HrU-xrUnb8g
# contest时直接brutal force了，应该用hua hua的方法：左边小的个数 * 右边大的个数 + 左边大的个数 * 右边小的个数 (其中左边大的个数=左边总个数-左边小的个数，同理右边)
class Solution(object):
    # brutal force
    def numTeams(self, rating):
        self.increase = 0
        self.decrease = 0

        def dfsIncrease(tmp, idx, rating):
            if len(tmp) == 3:
                self.increase += 1
                return
            for i in range(idx, len(rating)):
                if rating[i] > tmp[-1]:
                    tmp.append(rating[i])
                    dfsIncrease(tmp, i + 1, rating)
                    tmp.pop()
        for j in range(len(rating) - 2):
            dfsIncrease([rating[j]], j + 1, rating)

        def dfsDecrease(tmp, idx, rating):
            if len(tmp) == 3:
                self.decrease += 1
                return
            for i in range(idx, len(rating)):
                if rating[i] < tmp[-1]:
                    tmp.append(rating[i])
                    dfsDecrease(tmp, i + 1, rating)
                    tmp.pop()
        for j in range(len(rating) - 2):
            dfsDecrease([rating[j]], j + 1, rating)
        return self.increase + self.decrease

test = Solution()
print test.numTeams([2,5,3,4,1])
print test.numTeams([2,1,3])
print test.numTeams([1,2,3,4])