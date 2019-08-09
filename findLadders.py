import string
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []

        self.res = []
        self.step = float('inf')
        aToz = string.ascii_lowercase

        def dfs(tmp, wordSet, endWord):
            if len(tmp) > self.step:
                return
            curr = tmp[-1]
            if curr == endWord:
                if self.step == len(tmp):
                    self.res.append(tmp)
                else:
                    self.step = len(curr)
                    self.res = [tmp]
            for i in range(len(curr)):
                for l in aToz:
                    newCurr = curr[:i] + l + curr[i + 1:]
                    if newCurr in wordSet:
                        wordSet.remove(newCurr)
                        dfs(tmp + [newCurr], wordSet, endWord)
                        wordSet.add(newCurr)

        dfs([beginWord], set(wordList), endWord)
        return self.res

test = Solution()
print test.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])