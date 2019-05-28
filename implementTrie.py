class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.isWord = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            # move to child
            node = node.children[i]
        # Mark this is a word at the last node
        node.isWord = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.isWord

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
# print trie.search("somestring")
# print trie.startsWith("s")