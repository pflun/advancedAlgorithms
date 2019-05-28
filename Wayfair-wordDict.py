# -*- coding: utf-8 -*-
# 给一个dict和一堆字符，问那些字符能组成dict里哪些词，follow up是dict太大怎么办，用trie把dict存起来就好

class Solution(object):
    def wordDict(self, words, chars):
        res = []
        dic_c = {}
        for char in chars:
            dic_c[char] = dic_c.get(char, 0) + 1

        for word in words:
            dic_w = {}
            for w in word:
                dic_w[w] = dic_w.get(w, 0) + 1
            if dic_w == dic_c:
                res.append(word)

        return res


test = Solution()
print test.wordDict(["practice", "converse", "perfect", "coding", "conserve"], ['c', 'o', 'n', 's', 'e', 'r', 'v', 'e'])