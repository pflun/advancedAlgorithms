class Solution(object):
    def wordDistance(self, words, word1, word2):
        res = index1 = index2 = len(words)

        for i in range(len(words)):
            if words[i] == word1:
                index1 = i
                res = min(res, abs(index1 - index2))
            elif words[i] == word2:
                index2 = i
                res = min(res, abs(index1 - index2))

        return res

class Solution2(object):
    def shortestDistance(self, words, word1, word2):
        res = float('inf')
        index1 = -1
        index2 = -1

        for i in range(len(words)):
            if words[i] == word1:
                index1 = i
            if words[i] == word2:
                index2 = i
            if index1 != -1 and index2 != -1:
                res = min(res, abs(index1 - index2))

        return res

test = Solution()
print test.wordDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'practice')
