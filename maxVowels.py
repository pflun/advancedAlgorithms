class Solution(object):
    def maxVowels(self, s, k):
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        res = 0
        cnt = 0
        for c in s[:k]:
            if c in vowels:
                cnt += 1
        res = max(res, cnt)
        for i in range(k, len(s)):
            if cnt > 0 and s[i - k] in vowels:
                cnt -= 1
            if s[i] in vowels:
                cnt += 1
            res = max(res, cnt)
        return res

test = Solution()
print test.maxVowels("abciiidef", 3)
print test.maxVowels("aeiou", 2)
print test.maxVowels("leetcode", 3)
print test.maxVowels("rhythms", 4)
print test.maxVowels("tryhard", 4)
print test.maxVowels("novowels", 1)
print test.maxVowels("tnfazcwrryitgacaabwm", 4)