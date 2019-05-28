# -*- coding: utf-8 -*-
# 非brutal force，把words加入dict，对于words里面每一个word，reversed(word)然后在dict里找wordRvs，如果形成palindrome就应该存在
#
# brutal force, permute + isPalindrome
class Solution(object):
    def palindromePairs(self, words):
        self.res = []
        self.used = [False] * len(words)

        def dfs(words, tmp):
            if len(tmp) == 2:
                # deep copy
                candidate = ''.join(tmp[:])
                if isPalindrome(candidate):
                    self.res.append(candidate)

            for i in range(len(words)):
                if self.used[i]:
                    continue
                self.used[i] = True
                tmp.append(words[i])
                dfs(words, tmp)
                self.used[i] = False
                tmp.pop()

        def isPalindrome(s):
            # Rm punctuation, space and lowercase
            import string
            s = "".join(l for l in s if l not in string.punctuation).replace(" ", "").lower()
            # s = list(s)
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        dfs(words, [])
        return self.res

test = Solution()
print test.palindromePairs(["abcd","dcba","lls","s","sssll"])