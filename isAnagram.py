class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        d1, d2 = {}, {}
        for i in s:
            d1[i] = d1.get(i, 0) + 1

        for j in t:
            d2[j] = d2.get(j, 0) + 1

        return d1 == d2

test = Solution()
print test.isAnagram("rat", "car")