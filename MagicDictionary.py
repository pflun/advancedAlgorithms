# -*- coding: utf-8 -*-
# 可以把words按length存起来然后每有词想search时候遍历查找相符。
class MagicDictionary(object):

    def __init__(self):
        self.dic = {}

    def buildDict(self, dict):
        for w in dict:
            self.dic[len(w)] = self.dic.get(len(w), [] + [w])

    def search(self, word):
        cnt = 0
        i = 0
        if len(word) not in self.dic:
            return False
        for w in self.dic[len(word)]:
            while i < len(word):
                if cnt > 1:
                    break
                if word[i] != w[i]:
                    cnt += 1
                i += 1
            if cnt == 1:
                return True
        return False

obj = MagicDictionary()
obj.buildDict(["hello", "leetcode"])
print obj.search("hello")
print obj.search("hhllo")
print obj.search("hell")
print obj.search("leetcoded")