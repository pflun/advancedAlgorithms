# -*- coding: utf-8 -*-
import collections
import string
class Solution(object):
    # BFS拿到parents dict，DFS反推paths
    def findLadders3(self, beginWord, endWord, wordList):
        # {parent: set(children)}
        parents = collections.defaultdict(set)
        wordList = set(wordList)
        visited = set([beginWord])
        queue = [beginWord]
        while queue:
            size = len(queue)
            level_visited = set()
            for _ in range(0, size):
                # convert to list to replace letter
                curr = list(queue.pop(0))
                for i in range(len(beginWord)):
                    for j in range(ord('a'), ord('z') + 1):
                        newWord = curr[:i] + [chr(j)] + curr[i + 1:]
                        if ''.join(newWord) in wordList and ''.join(newWord) not in visited:
                            # build parents graph
                            parents[''.join(newWord)].add(''.join(curr))
                            level_visited.add(''.join(newWord))
                            queue.append(''.join(newWord))
            visited.update(level_visited)
            # 找到endWord，退出BFS
            if endWord in parents:
                break
        # DFS
        res = []
        def dfs(currWord, tmpPath):
            if currWord == beginWord:
                # 因为我们是从后往前推的，所以要把路径翻转一下再加入结果
                res.append(tmpPath[::-1])
                return
            for parent in parents[currWord]:
                tmpPath.append(parent)
                dfs(parent, tmpPath)
                tmpPath.pop()
        dfs(endWord, [endWord])
        return res

    def findLadders2(self, beginWord, endWord, wordList):
        aToz = string.ascii_lowercase
        res = []
        wordList = set(wordList)
        # current word: [path_to_current]
        transfer = {beginWord: [[beginWord]]}

        while transfer:
            tmp = {}
            for w in transfer.keys():
                if w == endWord:
                    for r in transfer[w]:
                        res.append(r)
                else:
                    for i in range(len(w)):
                        for c in aToz:
                            new_word = w[:i] + c + w[i + 1:]
                            if new_word in wordList:
                                tmp[new_word] = tmp.get(new_word, []) + [j + [new_word] for j in transfer[w]]

            for w in set(tmp.keys()):
                wordList.remove(w)
            transfer = tmp

        return res

    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []

        self.res = []
        self.step = float('inf')
        aToz = string.ascii_lowercase

        def dfs(tmp, wordSet, endWord):
            if len(tmp) > self.step:
                return
            curr = tmp[-1]
            if curr == endWord:
                if self.step == len(tmp):
                    self.res.append(tmp)
                else:
                    self.step = len(curr)
                    self.res = [tmp]
            for i in range(len(curr)):
                for l in aToz:
                    newCurr = curr[:i] + l + curr[i + 1:]
                    if newCurr in wordSet:
                        wordSet.remove(newCurr)
                        dfs(tmp + [newCurr], wordSet, endWord)
                        wordSet.add(newCurr)

        dfs([beginWord], set(wordList), endWord)
        return self.res

test = Solution()
print test.findLadders2("hit", "cog", ["hot","dot","dog","lot","log","cog"])