class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        dic1 = {}
        dic2 = {}
        for pair in pairs:
            dic1[pair[0]] = pair[1]
            dic2[pair[1]] = pair[0]

        for i in range(len(words1)):
            if words1[i] == words2[i] or dic1[words1[i]] == words2[i] or dic2[words1[i]] == words2[i]:
                continue
            else:
                return False
        return True

test = Solution()
print test.areSentencesSimilar(["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "fine"], ["acting", "drama"], ["skills", "talent"]])