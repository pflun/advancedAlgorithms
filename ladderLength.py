# -*- coding: utf-8 -*-
# BFS for every letter from A to Z, time complexity: n * 26 ^ l
# BFS用queue，每次pop(0)，对于curr每一位暂存(for backtracking)替换从A to Z，看看是不是end，如果是在dict里就加入queue继续BFS
# 外层queue类似level order traversal，每一层step + 1

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        queue = [beginWord]
        l = len(beginWord)
        step = 0

        while queue:
            step += 1
            size = len(queue)
            for _ in range(0, size):
                # convert to list to replace letter
                curr = list(queue.pop(0))
                # for each letter in curr word
                print wordList
                print queue
                for i in range(l):
                    # store tmp for backtrack (add back later)
                    tmp = curr[i]
                    # replace letter from a to z
                    for j in range(ord('a'), ord('z') + 1):
                        curr[i] = chr(j)
                        # if Found target
                        if ''.join(curr) == endWord:
                            return step + 1
                        # if not in dict
                        if ''.join(curr) not in wordList:
                            continue
                        # Optimize: word in dict can only use once
                        wordList.remove(''.join(curr))
                        # BFS append curr to queue
                        queue.append(''.join(curr))

                    # Add tmp back
                    curr[i] = tmp

        return 0

test = Solution()
print test.ladderLength("hit", "cog", ["hot","dot","dog","lot","log", "cog"])