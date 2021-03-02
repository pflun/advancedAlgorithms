# -*- coding: utf-8 -*-
class Solution(object):
    def decodeString2(self, s):
        stack = []
        curNum = 0
        curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curString += c
        return curString

    def decodeString(self, s):
        stack = []
        currNum = 1
        currString = ''
        i = 0
        while i < len(s):
            if s[i].isdigit():
                currNum = int(s[i])
                while i + 1 < len(s) and s[i + 1].isdigit():
                    currNum = currNum * 10 + int(s[i + 1])
                    i += 1
            elif s[i] == '[':
                stack.append(currString)
                stack.append(currNum)
                currNum = 1
                currString = ''
            elif s[i] == ']':
                num = stack.pop()
                prevString = stack.pop()
                currString = prevString + num * currString
            else:
                currString += s[i]
            i += 1
        return currString

test = Solution()
print test.decodeString("3[a2[c]]")