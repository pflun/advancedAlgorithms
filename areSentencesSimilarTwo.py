class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        dic = {}
        for p in pairs:
            dic[p[0]] = p[1]

        for i in range(len(words1)):
            w1 = words1[i]
            w2 = words2[i]
            if w1 == w2:
                continue
            else:
                exist = 0
                while w1 in dic:
                    w1_similar = dic[w1]
                    if w1_similar == w2:
                        exist = 1
                        break
                    w1 = w1_similar
                while w2 in dic:
                    w2_similar = dic[w2]
                    if w2_similar == w1:
                        exist = 1
                        break
                    w2 = w2_similar
                if exist:
                    continue
                else:
                    return False
        return True

test = Solution()
print test.areSentencesSimilarTwo( ["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]])