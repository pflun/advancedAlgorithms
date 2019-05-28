# -*- coding: utf-8 -*-
class Solution(object):
    def findSubstring(self, s, words):
        res = []
        dic = {}
        for word in words:
            dic[word] = 0

        for i in range(len(s) - len(words[0]) * len(words) + 1):
            if self.helper(s[i:i + len(words[0]) * len(words)], words, dic.copy()):
                res.append(i)

        return res

    def helper(self, str, words, dic):
        strList = []
        # substring裂解成list
        for i in range(len(words)):
            # foo, bar: [1 * 3:1 * 3 + 3]
            strList.append(str[i * len(words[0]):i * len(words[0]) + len(words[0])])
        # dic统计出现次数
        for string in strList:
            if string in dic:
                dic[string] += 1
        # words中每一个都出现过有且仅有一次
        return all(c == 1 for c in dic.values())

test = Solution()
print test.findSubstring("barfoothefoobarman", ["foo","bar"])