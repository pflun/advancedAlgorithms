class TrieNode():
    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return
        if word[0] != '.':
            if word[0] in node.children:
                curr = node.children[word[0]]
                self.dfs(curr, word[1:])
            else:
                return
        else:
            for n in node.children.values():
                self.dfs(n, word[1:])

test = WordDictionary()
print test.addWord("bad")
print test.addWord("dad")
print test.addWord("mad")
print test.search("dad")
print test.search(".ad")