class Solution(object):
    # First forward pass to find shortest distant to character on left.
    # Second backward pass to find shortest distant to character on right.
    def shortestToChar(self, s, c):
        toLeft = []
        toRight = []
        lastPos = float('-inf')
        for i in range(len(s)):
            if s[i] == c:
                lastPos = i
                toLeft.append(0)
            else:
                toLeft.append(i - lastPos)
        lastPos = float('inf')
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                lastPos = i
                toRight.append(0)
            else:
                toRight.append(lastPos - i)
        toRight = toRight[::-1]
        # you may combine third loop with the second loop
        res = []
        for i in range(len(s)):
            res.append(min(toLeft[i], toRight[i]))
        return res

test = Solution()
print test.shortestToChar("loveleetcode", "e")
print test.shortestToChar("aaab", "b")