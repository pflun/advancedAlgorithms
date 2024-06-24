# -*- coding: utf-8 -*-
class Solution(object):
    def removeDuplicateLetters(self, s):
        dic = {}
        visited = set()
        stack = []
        res = ''
        for i in range(len(s)):
            dic[s[i]] = i
        for i in range(len(s)):
            if s[i] not in visited:
                # stack内保持递增，如果之前的char不是最后一次出现，就被后面更小的顶替掉 lexicographical increasing
                while stack and i < dic[s[stack[-1]]] and s[i] <= s[stack[-1]]:
                    visited.remove(s[stack[-1]])
                    stack.pop()
                stack.append(i)
                visited.add(s[i])
        for i in range(len(stack)):
            res += s[stack[i]]
        return res

test = Solution()
print test.removeDuplicateLetters("bcabc")
print test.removeDuplicateLetters("cbacdcbc")
print test.removeDuplicateLetters("bbcaac")
print test.removeDuplicateLetters("abacb")