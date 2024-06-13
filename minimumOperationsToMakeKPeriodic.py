class Solution(object):
    def minimumOperationsToMakeKPeriodic(self, word, k):
        dic = {}
        i = 0
        while i < len(word):
            dic[word[i:i + k]] = dic.get(word[i:i + k], 0) + 1
            i += k
        highestFrq = 0
        for v in dic.values():
            highestFrq = max(highestFrq, v)
        return len(word) / k - highestFrq