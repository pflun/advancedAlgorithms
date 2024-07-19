class Solution(object):
    def numberOfSpecialChars(self, word):
        # last pos of lowercase occurrence
        dic_lower = {}
        # first pos of uppercase occurrence
        dic_upper = {}
        for i in range(len(word)):
            if word[i].islower():
                dic_lower[word[i]] = i
            else:
                if word[i] not in dic_upper:
                    dic_upper[word[i]] = i
        res = 0
        for k, v in dic_lower.items():
            k_upper = k.upper()
            if k_upper in dic_upper and v < dic_upper[k_upper]:
                res += 1
        return res

test = Solution()
print test.numberOfSpecialChars("aaAbcBC")
print test.numberOfSpecialChars("abc")
print test.numberOfSpecialChars("AbBCab")