# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=ptlwluzeC1I
# 计划递归，self.mem存之前结果
# Divide and Conquer
# helper('lee') and wordDict('tcode')
# helper('leet') and wordDict('code')

class Solution(object):
    def wordBreak(self, s, wordDict):
        self.mem = {}
        wordDict = set(wordDict)

        def helper(s, wordDict):
            # if substr can be found in mem (previous calculation)
            if s in self.mem and self.mem[s]:
                return True
            # if substr in set
            elif s in wordDict:
                self.mem[s] = True
                return True

            for i in range(1, len(s)):
                left = helper(s[:i], wordDict)
                # Note: recursion on right output correct result BUT way more time spent
                # right = helper(s[i:], wordDict)
                right = False
                if s[i:] in wordDict:
                    right = True

                # if left and right (and their substr) both can be found in set
                if left and right:
                    self.mem[s] = True
                    return True

            self.mem[s] = False
            print self.mem.items()
            return False

        return helper(s, wordDict)


test = Solution()
print test.wordBreak('leetcode', ['leet', 'code'])