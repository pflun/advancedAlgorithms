# -*- coding: utf-8 -*-
# 给一个list，一个set，问这个list里面有没有一个Subarray能够包含所有set里面的数
# 求最短subarray包含所有set
class Solution(object):
    def subarraySet(self, arr, target):
        dic = {}
        res = flaot('inf')
        left = 0
        for i in range(len(arr)):
            if arr[i] in target:
                dic[arr[i]] = dic.get(arr[i], 0) + 1
                if len(dic) == len(target):
                    res = min(res, i - left)
                    dic[arr[left]] = dic.get(arr[left]) - 1
                    left += 1
        return res