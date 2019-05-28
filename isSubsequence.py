# -*- coding: utf-8 -*-
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        i, j = 0, 0
        # j每次都走，i只有相等时走
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        # i有没有走到最后（和s长度相等）
        return True if i == len(s) else False