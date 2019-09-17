# -*- coding: utf-8 -*-
class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False
        self.times = 0

class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.data = ''
        self.res = []
        self.root = TrieNode(0)
        for i in range(len(sentences)):
            self.build(sentences[i], times[i])

    def build(self, sentence, time):
        node = self.root
        for s in sentence:
            if s not in node.children:
                node.children[s] = TrieNode(s)
            node = node.children[s]
        node.isWord = True
        node.times = time

    def input(self, c):
        if c == '#':
            self.build(self.data, 1)
            self.data = ''
            return []
        self.data += c
        self.search()
        # use heap to get top 3, 懒得写了
        return self.res

    def search(self):
        node = self.root
        for i in self.data:
            if i not in node.children:
                return []
            node = node.children[i]
        for c in node.children.values():
            self.dfs(self.data, c)
        return res

    def dfs(self, tmp, node):
        if node.isWord:
            self.res.append(tmp[:])
        for c in node.children.values():
            tmp += c.val
            dfs(tmp, c)
            tmp = tmp[:-1]