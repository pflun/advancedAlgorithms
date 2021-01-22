# -*- coding: utf-8 -*-
# https://leetcode.com/problems/word-search-ii/discuss/59790/Python-dfs-solution-(directly-use-Trie-implemented).
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord

class Solution(object):
    def findWords3(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i + 1, j, path + tmp, res)
        self.dfs(board, node, i - 1, j, path + tmp, res)
        self.dfs(board, node, i, j - 1, path + tmp, res)
        self.dfs(board, node, i, j + 1, path + tmp, res)
        board[i][j] = tmp

    def findWords(self, board, words):
        self.res = []

        def dfs(board, i, j, depth, word):
            # 出界，depth为0，当前cell不等于word当前位
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or depth == 0 or board[i][j] != word[len(word) - depth]:
                return
            if depth == 1:
                self.res.append(word)

            # same letter cell may not be used more than once, backtracking
            tmp = board[i][j]
            board[i][j] = "#"
            dfs(board, i + 1, j, depth - 1, word)
            dfs(board, i - 1, j, depth - 1, word)
            dfs(board, i, j + 1, depth - 1, word)
            dfs(board, i, j - 1, depth - 1, word)
            board[i][j] = tmp


        for word in words:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    dfs(board, i, j, len(word), word)

        return self.res

    def findWords2(self, board, words):
        self.res = []
        self.dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(board, tmp, target, visited, i, j):
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or (i, j) in visited or board[i][j] != target[0]:
                return
            target = target[1:]
            tmp += board[i][j]
            visited.add((i, j))
            if len(target) == 0:
                self.res.append(tmp)
                return
            for d in self.dir:
                x = i + d[0]
                y = j + d[1]
                dfs(board, tmp, target, visited, x, y)
            visited.remove((i, j))

        for word in words:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    dfs(board, '', word, set(), i, j)

        return self.res

test = Solution()
print test.findWords2(
 [['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']], ["oath","pea","eat","rain"])