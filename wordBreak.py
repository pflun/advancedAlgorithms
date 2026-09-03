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
            # If substr can be found in mem (previous calculation)
            # Return True if prev calculation is True, False if prev calculation prove not in wordDict
            if s in self.mem:
                return self.mem[s]
            # if substr in set
            elif s in wordDict:
                self.mem[s] = True
                return True

            for i in range(1, len(s)):
                left = helper(s[:i], wordDict)
                right = helper(s[i:], wordDict)
                # if left and right (and their substr) both can be found in set
                if left and right:
                    self.mem[s] = True
                    return True

            self.mem[s] = False
            return False

        return helper(s, wordDict)


test = Solution()
print test.wordBreak('leetcode', ['leet', 'code'])

# Note: recursion on right output correct result BUT way more time spent
# We can replace line: right = helper(s[i:], wordDict) with
# right = False
# if s[i:] in wordDict:
#     right = True