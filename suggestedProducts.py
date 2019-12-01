from collections import OrderedDict
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.word = ''
        self.isWord = False
        self.children = OrderedDict()

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        products.sort()
        self.root = TrieNode()
        for p in products:
            self.insert(p)
        res = []
        self.node = self.root
        for c in searchWord:
            if c in self.node.children:
                tmp = self.search(self.node.children[c], [], 'c')
                self.node = self.node.children[c]
                res.append(tmp)
            else:
                res.append([])
        return res

    def search(self, node, cache, tmp):
        if len(cache) == 3:
            return cache
        if node.isWord:
            cache.append(node.word)
        for n in node.children.values():
            tmp = n.word
            self.search(n, cache, tmp)
        return cache

    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        # Mark this is a word at the last node
        node.isWord = True
        node.word = word

test = Solution()
print test.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse")
print test.suggestedProducts(["havana"], "havana")
print test.suggestedProducts(["bags","baggage","banner","box","cloths"], "bags")
print test.suggestedProducts(["havana"], "tatiana")