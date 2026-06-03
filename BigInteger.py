# -*- coding: utf-8 -*-
class BigInteger(object):
    def __init__(self, num):
        # 你的原始初始化逻辑
        self.isPositive = False if str(num)[0] == '-' else True
        self.val = str(num) if self.isPositive else str(num)[1:]

class Solution(object):
    def add(self, num1, num2):
        # 1. 符号相同，做纯加法
        if num1.isPositive == num2.isPositive:
            res_val = self._add_strings(num1.val, num2.val)
            if num1.isPositive:
                return res_val
            else:
                return '-' + res_val
                
        # 2. 符号不同，做大数减小数
        # 如果两个绝对值完全一样大，直接返回 0
        if num1.val == num2.val:
            return '0'
            
        # 根据返回的 boolean 决定谁减谁
        if self._is_greater_or_equal(num1.val, num2.val):
            # num1 绝对值更大，用 num1 减 num2，结果符号跟随 num1
            res_val = self._sub_strings(num1.val, num2.val)
            if num1.isPositive:
                return res_val
            else:
                return '-' + res_val
        else:
            # num2 绝对值更大，用 num2 减 num1，结果符号跟随 num2
            res_val = self._sub_strings(num2.val, num1.val)
            if num2.isPositive:
                return res_val
            else:
                return '-' + res_val

    def _is_greater_or_equal(self, s1, s2):
        """判断绝对值 s1 是否 >= s2"""
        if len(s1) > len(s2):
            return True
        elif len(s1) < len(s2):
            return False
        else:
            return s1 >= s2

    def _add_strings(self, s1, s2):
        res = ''
        carry = 0
        i = 0
        n1 = s1[::-1]
        n2 = s2[::-1]
        
        while i < max(len(n1), len(n2)):
            if i >= len(n1):
                v1 = 0
            else:
                v1 = int(n1[i])
            if i >= len(n2):
                v2 = 0
            else:
                v2 = int(n2[i])
                
            carry, curr = divmod(v1 + v2 + carry, 10)
            res = str(curr) + res
            i += 1
            
        if carry == 1:
            return '1' + res
        else:
            return res

    def _sub_strings(self, s1, s2):
        res = ''
        borrow = 0
        i = 0
        n1 = s1[::-1]
        n2 = s2[::-1]
        
        # 因为我们确保了 s1 >= s2，所以只用遍历到 len(n1)
        while i < len(n1):
            v1 = int(n1[i])
            if i >= len(n2):
                v2 = 0
            else:
                v2 = int(n2[i])
                
            # 利用 Python divmod 对负数向下取整的特性，巧妙处理借位
            q, curr = divmod(v1 - v2 - borrow, 10)
            borrow = -q
            
            res = str(curr) + res
            i += 1
            
        # 去掉减法产生的前导 0
        res = res.lstrip('0')
        if res == '':
            return '0'
        return res

# 测试代码
test = Solution()

num1 = BigInteger('25')
num2 = BigInteger('-101')
print test.add(num1, num2)       # 预期: -76
print test.add(num2, num1)       # 预期: -76

num3 = BigInteger('101')
num4 = BigInteger('-25')
print test.add(num3, num4)       # 预期: 76

num5 = BigInteger('-25')
num6 = BigInteger('-101')
print test.add(num5, num6)       # 预期: -126

num7 = BigInteger('100')
num8 = BigInteger('-100')
print test.add(num7, num8)       # 预期: 0