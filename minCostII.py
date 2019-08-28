# -*- coding: utf-8 -*-
# https://www.cnblogs.com/grandyang/p/5322870.html
class Solution(object):
    def minCostII(self, costs):
        min1 = 0
        min2 = 0
        lastColor = -1
        for i in range(len(costs)):
            currMin1 = float('inf')
            currMin2 = float('inf')
            currColor = -1
            for k in range(len(costs[i])):
                # 同色用第二小的值
                if k == lastColor:
                    newCost = costs[i][k] + min2
                else:
                    newCost = costs[i][k] + min1
                if newCost < currMin1:
                    currMin2 = currMin1
                    currMin1 = newCost
                    currColor = k
                elif newCost < currMin2:
                    currMin2 = newCost
            min1 = currMin1
            min2 = currMin2
            lastColor = currColor

        return min1

test = Solution()
print test.minCostII([[1,5,3],[2,9,4]])