class Solution(object):
    # need to add memory otherwise TLE
    def findAllConcatenatedWordsInADict(self, words):
        targets = set(words)

        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in targets and suffix in targets:
                    return True
                if prefix in targets and dfs(suffix):
                    return True
                if suffix in targets and dfs(prefix):
                    return True

            return False

        res = []
        for word in words:
            if dfs(word):
                res.append(word)

        return res

test = Solution()
print test.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])
print test.findAllConcatenatedWordsInADict(["cat","dog","catdog"])