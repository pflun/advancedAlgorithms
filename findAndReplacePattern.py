class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        dp = {}
        res = []
        for i in range(len(pattern)):
            dp[pattern[i]] = dp.get(pattern[i], []) + [i]

        for word in words:
            dw = {}
            for i in range(len(word)):
                dw[word[i]] = dw.get(word[i], []) + [i]
            if sorted(dp.values()) == sorted(dw.values()):
                res.append(word)

        return res

test = Solution()
print test.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb")