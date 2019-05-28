# -*- coding: utf-8 -*-
class Solution(object):
    def letterCasePermutation(self, S):
        self.res = []

        queue = [S[0]]
        # i指向S的某一位
        i = 0

        # BFS，生成大小写string再加入queue，用levelOrder方式移动i指向下一个字母
        while queue:
            i += 1
            size = len(queue)
            for _ in range(0, size):
                curr = queue.pop(0)
                # 找到一个解
                if len(curr) == len(S):
                    self.res.append(curr)
                elif len(curr) < len(S) and i < len(S):
                    if curr[-1].isalpha():
                        # curr末位如果是字母，生成大小写string再加入queue
                        up = ''.join(list(curr[:-1]) + [curr[-1].upper()] + [S[i]])
                        low = ''.join(list(curr[:-1]) + [curr[-1].lower()] + [S[i]])
                        queue.append(up)
                        queue.append(low)
                    else:
                        queue.append(curr + S[i])

        return self.res

test = Solution()
print test.letterCasePermutation("a1b2")
