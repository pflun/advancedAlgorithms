class Solution(object):
    def reorderSpaces(self, text):
        res = ""
        spaces = 0
        words = text.split()
        for i in range(len(text)):
            if text[i] == " ":
                spaces += 1
        if len(words) == 1:
            return words[0] + (' ' * spaces)
        spNum = spaces / (len(words) - 1)
        reminder = spaces % (len(words) - 1)
        sp = ''
        for _ in range(spNum):
            sp += ' '
        for i in range(len(words)):
            res += words[i]
            if i != len(words) - 1:
                res += sp
        if reminder != 0:
            for _ in range(reminder):
                res += ' '
        return res

test = Solution()
print test.reorderSpaces("  this   is  a sentence ")
print test.reorderSpaces(" practice   makes   perfect")
print test.reorderSpaces("hello   world")
print test.reorderSpaces("a")
