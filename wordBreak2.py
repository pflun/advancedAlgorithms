# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=ptlwluzeC1I
# 计划递归，self.mem存之前结果
# Divide and Conquer
# helper('lee') and wordDict('tcode')
# helper('leet') and wordDict('code')

class Solution(object):
    def wordBreak2(self, s, wordDict):
        self.mem = {}
        self.res = []
        self.size = len(s)
        wordDict = set(wordDict)

        def helper(s, wordDict):
            # if substr can be found in mem (previous calculation)
            if s in self.mem and self.mem[s]:
                return s
            # if substr in set
            elif s in wordDict:
                self.mem[s] = True
                return s

            for i in range(1, len(s)):
                left = helper(s[:i], wordDict)
                right = False
                if s[i:] in wordDict:
                    right = s[i:]

                # if left and right (and their substr) both can be found in set
                if left and right:
                    self.mem[s] = True
                    tmp = left + ' ' + right
                    if len(tmp.replace(" ", "")) == self.size:
                        self.res.append(tmp)
                    else:
                        return tmp


            self.mem[s] = False
            print self.mem.items()
            return False

        helper(s, wordDict)
        return self.res

# Need debug
test = Solution()
print test.wordBreak2('catsanddog', ["cat", "cats", "and", "sand", "dog"])


class Solution2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res

test = Solution2()
print test.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"])