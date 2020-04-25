# -*- coding: utf-8 -*-
# https://www.geeksforgeeks.org/minimum-word-break/
# 一开始把0放入Queue中。当Queue不为空时，拿出下一个index，然后有个内部循环，临时变量i=从index开始一直到S.length()，取从index开始到i(exclusive)的substring，
# 检查是不是在Dictionary里面，如果在，则看i是不是已经到S的结尾了，如果是，则返回counter，不是，则把i offer进queue。当然，如果i是已在set中，就可以跳过。出了这个内部循环之后，counter++
class Solution(object):
    def minWordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        queue = [0]
        step = 1
        visited = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                visited.add(curr)
                for i in range(curr, len(s) + 1):
                    if s[curr:i] in wordSet:
                        if i == len(s):
                            return step
                        if i not in visited:
                            queue.append(i)
            step += 1
        return

test = Solution()
print test.minWordBreak('leetcode', ['leet', 'code'])