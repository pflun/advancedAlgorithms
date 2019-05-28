class Solution:
    # @param {string} s a string
    # @param {string} t a string
    # @return {boolean} true if the characters in s
    # can be replaced to get t or false
    def isIsomorphic(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
            print d1
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
            print d2
        return sorted(d1.values()) == sorted(d2.values())

    def isIsomorphic2(self, s, t):
        if len(s) != len(t):
            return False

        d1, d2 = {}, {}
        for i in range(len(s)):
            if s[i] in d1:
                d1[s[i]].append(i)
            else:
                d1[s[i]] = [i]
        for i in range(len(t)):
            if t[i] in d2:
                d2[t[i]].append(i)
            else:
                d2[t[i]] = [i]
        if sorted(d1.values()) == sorted(d2.values()):
            return True
        else:
            return False

test = Solution()
print test.isIsomorphic2("paper", "title")