# -*- coding: utf-8 -*-
# 因为会多次调用，我们不能每次调用的时候再把这两个单词的下标找出来。我们可以用一个哈希表，在传入字符串数组时，就把每个单词的下标找出存入表中。
# 这样当调用最短距离的方法时，我们只要遍历两个单词的下标列表就行了。
class WordDistance(object):
    def __init__(self, words):
        self.dic = {}
        for i, w in enumerate(words):
            self.dic[w] = self.dic.get(w, []) + [i]

    def shortest(self, w1, w2):
        index1 = self.dic[w1]
        index2 = self.dic[w2]
        res = float('inf')
        for i in index1:
            for j in index2:
                res = min(res, abs(i - j))
        return res
        

test = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
print test.shortest('makes', 'practice')