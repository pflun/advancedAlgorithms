class Solution(object):
    def __init__(self, dictionary):
        self.dic = {}
        # i18l => ['international', 'intithational']
        for word in dictionary:
            if len(word) > 2:
                abbr = word[0] + str(len(word) - 2) + word[-1]
            else:
                abbr = word
            if abbr in self.dic:
                self.dic[abbr].append(word)
            else:
                self.dic[abbr] = [word]

    def isUnique(self, string):
        if len(string) > 2:
            abbr = string[0] + str(len(string) - 2) + string[-1]
        if abbr not in self.dic:
            return True
        # if in the one in dict is the word itself (same word)
        elif len(self.dic[abbr]) == 1 and string == self.dic[abbr][0]:

            return True

        return False

test = Solution(["deer", "door", "cake", "card"])
print test.isUnique("door")