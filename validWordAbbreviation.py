# -*- coding: utf-8 -*-
class Solution(object):
    def validWordAbbreviation(self, word, abbr):

        def getNum(i, abbr):
            for j in range(i, len(abbr)):
                if not abbr[j].isdigit():
                    break
            return int(abbr[i:j])

        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            if not abbr[j].isdigit():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                increment = getNum(j, abbr)
                i += increment
                j += len(str(increment))

        return True if i == len(word) and j == len(abbr) else False

test = Solution()
print test.validWordAbbreviation("internationalization","i12iz4n")