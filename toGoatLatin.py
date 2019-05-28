class Solution(object):
    def toGoatLatin(self, S):
        vowel = set(["a", "e", "i", "o", "u"])
        res = S.split(" ")

        for i in range(len(res)):
            if res[i][0] in vowel:
                res[i] += "ma"
            else:
                res[i] = res[i][1:] + res[i][0] + "ma"
            res[i] += "a" * (i + 1)

        return res

test = Solution()
print test.toGoatLatin("I speak Goat Latin")