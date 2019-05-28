class Solution(object):
    def wordPattern(self, pattern, str):

        d1, d2 = {}, {}
        pattern = list(pattern)
        str = str.split()

        if len(str) != len(pattern):
            return False

        for i, val in enumerate(pattern):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(str):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())


test = Solution()
print test.wordPattern("abba", "dog cat cat dog")