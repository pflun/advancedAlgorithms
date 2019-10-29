# -*- coding: utf-8 -*-
class Solution(object):
    # 卧槽 可以任意组合
    def maxLength(self, arr):
        res = 0
        self.hashSet = set()
        l = 0
        r = 0
        while r < len(arr):
            if self.exist(arr[r]):
                for c in arr[l]:
                    self.hashSet.remove(c)
                l += 1
            else:
                for c in arr[r]:
                    self.hashSet.add(c)
                r += 1
            res = max(res, len(self.hashSet))
        return res

    def exist(self, s):
        for c in s:
            if c in self.hashSet:
                return True
        return False

test = Solution()
print test.maxLength(["un","iq","ue"])
print test.maxLength(["cha","r","act","ers"])