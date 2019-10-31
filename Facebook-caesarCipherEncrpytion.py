# -*- coding: utf-8 -*-
# https://leetcode.com/discuss/interview-question/395045/Facebook-or-Phone-Screen-or-Caesar-Cipher
#
# Question 1:
# Caesar Cipher Encrpytion
# You are given a list of string, group them if they are same after using
# Ceaser Cipher Encrpytion.
# Definition of "same", "abc" can right shift 1, get "bcd",
# here you can shift as many time as you want, the string will be considered as same.
#
# Example:
#
# Input: ["abc", "bcd", "acd", "dfg"]
# Output: [["abc", "bcd"], ["acd", "dfg"]]
class Solution(object):
    def caesarCipherEncrpytion(self, arr):
        self.dic = {}
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                tmp = self.isValid(arr[i], arr[j])
                if tmp:
                    self.dic[tmp] = self.dic.get(tmp, []) + [arr[i]]
                    self.dic[tmp].append(arr[j])
        res = []
        for v in self.dic.values():
            res.append(v)
        return res

    def isValid(self, s1, s2):
        if len(s1) != len(s2):
            return False
        diff = None
        for i in range(len(s1)):
            l1 = ord(s1[i])
            l2 = ord(s2[i])
            if diff is None:
                diff = l1 - l2
                continue
            else:
                if diff != l1 - l2:
                    return False
        return diff

test = Solution()
print test.isValid("acd", "abc")
print test.caesarCipherEncrpytion(["abc", "bcd", "acd", "dfg"])