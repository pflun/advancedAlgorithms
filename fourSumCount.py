# -*- coding: utf-8 -*-
class Solution(object):
    # Time Limit Exceeded
    def fourSumCount(self, A, B, C, D):
        res = 0

        AB = []
        CD = []

        for a in A:
            for b in B:
                AB.append(a + b)

        for c in C:
            for d in D:
                CD.append(c + d)

        for i in AB:
            for j in CD:
                if i + j == 0:
                    res += 1

        return res

    # TLE
    def fourSumCount2(self, A, B, C, D):
        res = 0
        dic1 = {}
        dic2 = {}

        for a in A:
            for b in B:
                dic1[a + b] = dic1.get(a + b, 0) + 1

        for c in C:
            for d in D:
                dic2[c + d] = dic2.get(c + d, 0) + 1

        for k1, v1 in dic1.items():
            for k2, v2 in dic2.items():
                if k1 + k2 == 0:
                    res += v1 * v2

        return res

    def fourSumCount3(self, A, B, C, D):
        res = 0
        dic = {}

        for a in A:
            for b in B:
                dic[a + b] = dic.get(a + b, 0) + 1

        for c in C:
            for d in D:
                if -c - d in dic:
                    res += dic[-c - d]

        return res

test = Solution()
print test.fourSumCount3([1, 2], [-2,-1], [-1, 2], [0, 2])