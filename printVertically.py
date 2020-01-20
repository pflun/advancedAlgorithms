class Solution(object):
    def printVertically(self, s):
        wordList = s.split(' ')
        maxLen = 0
        for w in wordList:
            maxLen = max(maxLen, len(w))
        res = ['' for _ in range(maxLen)]
        for i in range(len(wordList)):
            for j in range(len(wordList[i])):
                res[j] += wordList[i][j]
            if len(wordList[i]) < maxLen:
                for k in range(maxLen - 1, len(wordList[i]) - 1, -1):
                    res[k] += ' '
        rnt = []
        for r in res:
            rnt.append(r.rstrip())
        return rnt

test = Solution()
print test.printVertically("HOW ARE YOU")
print test.printVertically("TO BE OR NOT TO BE")
print test.printVertically("CONTEST IS COMING")