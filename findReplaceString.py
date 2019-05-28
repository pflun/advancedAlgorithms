# -*- coding: utf-8 -*-
# TreeMap存原string的index => 替换后的一个或多个char，多个char就对应的index补成空''
# 最后从index 1到index最大串起来
from collections import OrderedDict
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        dic = OrderedDict()
        res = ''
        for i in range(len(indexes)):
            if sources[i] == S[indexes[i]:indexes[i] + len(sources[i])]:
                dic[indexes[i]] = targets[i]
                if len(sources[i]) > 1:
                    for j in range(indexes[i] + 1, indexes[i] + len(sources[i])):
                        dic[j] = ""
        i = 0
        while i < len(S):
            if i not in dic:
                dic[i] = S[i]
            i += 1

        for k, v in sorted(dic.items()):
            res += v
        return res

test = Solution()
print test.findReplaceString("abcd", [0,2], ["a","cd"], ["eee","ffff"])
