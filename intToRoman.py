# -*- coding: utf-8 -*-
# 从高位向低位，这题巧在values array的构成
class Solution(object):
    def intToRoman(self, num):
        res = ''
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        strs = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                res += strs[i]

        return res

test = Solution()
print test.intToRoman(45)