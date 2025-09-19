import string
class Solution(object):
    def findLadders2(self, beginWord, endWord, wordList):
        aToz = string.ascii_lowercase
        res = []
        wordList = set(wordList)
        # current word: [path_to_current]
        transfer = {beginWord: [[beginWord]]}

        while transfer:
            tmp = {}
            for w in transfer.keys():
                if w == endWord:
                    for r in transfer[w]:
                        res.append(r)
                else:
                    for i in range(len(w)):
                        for c in aToz:
                            new_word = w[:i] + c + w[i + 1:]
                            if new_word in wordList:
                                tmp[new_word] = tmp.get(new_word, []) + [j + [new_word] for j in transfer[w]]

            for w in set(tmp.keys()):
                wordList.remove(w)
            transfer = tmp

        return res

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
print test.findLadders2("hit", "cog", ["hot","dot","dog","lot","log","cog"])