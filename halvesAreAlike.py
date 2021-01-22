class Solution(object):
    def halvesAreAlike(self, s):
        hashSet = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        s1 = s[:len(s) / 2]
        s2 = s[len(s) / 2:]
        cnt1 = 0
        cnt2 = 0
        for i in range(len(s1)):
            if s1[i] in hashSet:
                cnt1 += 1
            if s2[i] in hashSet:
                cnt2 += 1
        return True if cnt1 == cnt2 else False

test = Solution()
print test.halvesAreAlike("book")
print test.halvesAreAlike("textbook")
print test.halvesAreAlike("MerryChristmas")
print test.halvesAreAlike("AbCdEfGh")