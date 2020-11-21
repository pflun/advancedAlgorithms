class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        dic1 = {}
        dic2 = {}
        for w in word1:
            dic1[w] = dic1.get(w, 0) + 1
        for w in word2:
            dic2[w] = dic2.get(w, 0) + 1
        res1 = dic1.values()
        res2 = dic2.values()
        res1.sort()
        res2.sort()
        return True if res1 == res2 else False