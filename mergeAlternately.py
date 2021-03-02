class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = ''
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1
        if i == len(word1) and j == len(word2):
            return res
        elif i == len(word1):
            return res + word2[j:]
        else:
            return res + word1[i:]

test = Solution()
print test.mergeAlternately("abc", "pqr")
print test.mergeAlternately("ab", "pqrs")
print test.mergeAlternately("abcd", "pq")