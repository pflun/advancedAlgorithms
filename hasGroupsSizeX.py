# -*- coding: utf-8 -*-
class Solution(object):
    def hasGroupsSizeX(self, deck):
        if len(deck) < 2:
            return False

        dic = {}
        for num in deck:
            dic[num] = dic.get(num, 0) + 1

        res = dic.values()[0]
        # 求List GCD, for [1,1],[2,2],[2,2]
        for c in dic.values()[1::]:
            res = self.gcd(res, c)

        return False if res == 1 else True

    # greatest common divisor
    def gcd(self, x, y):
        if x % y == 0:
            return y
        else:
            return self.gcd(y, x % y)

test = Solution()
print test.hasGroupsSizeX([1,1,1,2,2,2,3,3])
