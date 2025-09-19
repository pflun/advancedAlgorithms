# -*- coding: utf-8 -*-
class Solution(object):
    def validWordAbbreviation(self, word, abbr):

        def getNum(i, abbr):
            j = i
            while j < len(abbr) and abbr[j].isdigit():
                j += 1

            if abbr[i] == "0" and j - i > 1:
                return False
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
                if increment is False:
                    return False
                i += increment
                j += len(str(increment))

        return True if i == len(word) and j == len(abbr) else False

test = Solution()
print test.validWordAbbreviation("internationalization","i18n")
print test.validWordAbbreviation("internationalization","i14at2n")
print test.validWordAbbreviation("internationalization","i12iz4n")
print test.validWordAbbreviation("internationalization","i144n")
print test.validWordAbbreviation("internationalization","i018n")
print test.validWordAbbreviation("internationalization","i01ternationalization")
print test.validWordAbbreviation("kubernetes", "k8s")
print test.validWordAbbreviation("invariability", "i4ia5y")
print test.validWordAbbreviation("python", "5")
print test.validWordAbbreviation("python", "6")
print test.validWordAbbreviation("python", "7")
print test.validWordAbbreviation("a", "1")
print test.validWordAbbreviation("1", "a")
print test.validWordAbbreviation("ks", "k0s")
print test.validWordAbbreviation("kes", "k0s")
print test.validWordAbbreviation("", "0") # ?
print test.validWordAbbreviation("a", "0a")
print test.validWordAbbreviation("a", "a0")