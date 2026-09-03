# -*- coding: utf-8 -*-
# 以  4 / 333  为例
# • 整数部分： 4 // 333 = 0 。加上小数点，当前结果： "0."
# • 初始余数： rem = 4
# 开始循环模拟竖式除法：
# 1. 第一步： rem = 4 ，没见过。
# • 记录到字典： seen[4] = 2 （因为此时  "0."  的长度是 2，我们要记住这个位置）。
# • 借位： 4 * 10 = 40 。
# • 算商： 40 // 333 = 0 ，贴到结果上，结果变  "0.0" 。
# • 算新余数： 40 % 333 = 40 。
# 2. 第二步： rem = 40 ，没见过。
# • 记录： seen[40] = 3 （此时  "0.0"  长度是 3）。
# • 借位： 40 * 10 = 400 。
# • 算商： 400 // 333 = 1 ，贴上去，结果变  "0.01" 。
# • 算新余数： 400 % 333 = 67 。
# 3. 第三步： rem = 67 ，没见过。
# • 记录： seen[67] = 4 。
# • 借位： 67 * 10 = 670 。
# • 算商： 670 // 333 = 2 ，贴上去，结果变  "0.012" 。
# • 算新余数： 670 % 333 = 4 。
# 4. 第四步（见证奇迹）： rem = 4 。
# • 等一下！ 字典里居然已经有  4  了！它第一次出现的 Index 是  seen[4] = 2 。
# • 也就是从下标  2  开始的所有数字，全都是循环部分！
# • 直接切片：把  "0."  (前2位) 和  "(012)"  拼起来 ->  "0.(012)" ，直接 return

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"
        res = []
        if numerator * denominator < 0:
            res.append("-")
        integer, remainder = divmod(abs(numerator), abs(denominator))
        res.append(str(integer))
        if remainder == 0:
            return "".join(res)
        res.append(".")
        dic = {}
        while remainder != 0:
            # 找到余数循环了
            if remainder in dic:
                res.insert(dic[remainder], "(")
                res.append(")")
                break
            dic[remainder] = len(res)
            # 借 10 算除法
            remainder *= 10
            res.append(str(remainder / abs(denominator)))
            remainder %= abs(denominator)
        return "".join(res)

test = Solution()
print test.fractionToDecimal(1, 2)
print test.fractionToDecimal(2, 1)
print test.fractionToDecimal(4, 333)
print test.fractionToDecimal(-1, 2)