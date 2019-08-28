# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=TqrZg4wYP1U
class Solution(object):
    def __init__(self):
        self.root = TrieNode()

    # Solution #1, brutal force
    def longestWord(self, words):
        res = ''
        s = set(words)

        for word in words:
            # 剪枝：如果当前长度已经小于res长度 or 同样长但lexicographical更大
            if len(word) < len(res) or len(word) == len(res) and word > res:
                continue
            prefix = ''
            valid = True
            # 把单词每个字符加到prefix上，查找prefix是否在set里，不在就利用valid退出循环
            for char in word:
                if valid is True:
                    prefix += char
                    if prefix not in s:
                        valid = False
            if valid is True:
                res = word

        return res

    # Solution #2, Trie
    def longestWordTrie(self, words):
        for w in words:
            self.insert(w)
        res = ''
        queue = [self.root]
        # BFS
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                for v in curr.children.values():
                    if v.isWord:
                        queue.append(v)
                        res = v.word

        return res

    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        # Mark this is a word at the last node
        node.isWord = True
        node.word = word

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.word = ''
        self.isWord = False
        self.children = {}

test = Solution()
print test.longestWordTrie(["a", "banana", "app", "appl", "ap", "apply", "apple"])