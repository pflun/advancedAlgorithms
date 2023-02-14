# -*- coding: utf-8 -*-
# 假设把所有人运到A city，再按照谁从A换到B能省更多钱，把一半人换到B city
class Solution(object):
    def twoCitySchedCost(self, costs):
        refund = []
        # 把人从A换到B的cost
        for c in costs:
            refund.append(c[1] - c[0])
        # 负得越多，省的越多
        refund.sort()
        res = 0
        # move all to city A
        for c in costs:
            res += c[0]
        for i in range(len(costs) / 2):
            res += refund[i]
        return res

test = Solution()
print test.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])
print test.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])
print test.twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]])