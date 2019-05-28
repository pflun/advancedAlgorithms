# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()

    def addWord(self, word):
        if word:
            self.set.add(word)

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            if word in self.set:
                return True
            else:
                return False
        # Tip: how to implement wildcard
        for w in self.set:
            for i in range(len(word)):
                # compare each char in word with each element in set, '.' allow pass
                if word[i] != w[i] and word[i] != '.':
                    break
            # "for...else..." loop fell through without finding a factor
            else:
                return True

        return False

obj = WordDictionary()
obj.addWord("word")
obj.addWord("work")
obj.addWord("wolf")
print obj.search(".ord")