class Solution(object):
    def wordSquares(self, words):
        self.res = []
        self.used = set()

        def dfs(words, tmp):
            if len(tmp) == 4:
                if self.isValidSquare(tmp):
                    self.res.append(tmp[:])
                return
            for i in range(len(words)):
                if words[i] in self.used:
                    continue
                self.used.add(words[i])
                tmp.append(words[i])
                dfs(words, tmp)
                tmp.pop()
                self.used.remove(words[i])
        dfs(words, [])
        return self.res

    def isValidSquare(self, words):
        for x in range(len(words[0])):
            tmp = ""
            for y in range(len(words)):
                tmp += words[y][x]
            if tmp != words[x]:
                return False
        return True

test = Solution()
print test.wordSquares(["area","lead","wall","lady","ball"])