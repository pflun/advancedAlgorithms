# For "abAcD", a reasonable answer is "acbAD"
class Solution:
    def sortLetters(self, chars):
        chars = list(chars)
        for i in range(len(chars)):
            if chars[i].islower():
                break
        for j in range(i, len(chars)):
            if chars[j].islower():
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
        return ''.join(chars)

test = Solution()
print test.sortLetters("abAcD")