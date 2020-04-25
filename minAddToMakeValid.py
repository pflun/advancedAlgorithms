# -*- coding: utf-8 -*-
class Solution(object):
    # two pass solution, 和1249 remove是一个道理
    def minAddToMakeValid2(self, S):
        res = 0
        cnt = 0
        i = 0
        while i < len(S):
            if S[i] == '(':
                cnt += 1
            elif S[i] == ')':
                cnt -= 1
            if cnt < 0:
                res += 1
                cnt += 1
            i += 1
        cnt = 0
        i = len(S) - 1
        while i >= 0:
            if S[i] == '(':
                cnt += 1
            elif S[i] == ')':
                cnt -= 1
            if cnt > 0:
                res += 1
                cnt -= 1
            i -= 1
        return res

    def minAddToMakeValid(self, S):
        step = 0
        queue = [S]

        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                if self.isValid(curr):
                    return step
                for i in range(len(curr) + 1):
                    queue.append(curr[:i] + '(' + curr[i:])
                    queue.append(curr[:i] + ')' + curr[i:])

            step += 1

    def isValid(self, s):
        stack = []
        dict = {")": "("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False

        if stack == []:
            return True

test = Solution()
print test.minAddToMakeValid2("(((")
print test.minAddToMakeValid2("()))((")
