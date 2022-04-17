class Solution(object):
    def maxValue(self, n, x):
        if n[0] == '-':
            for i in range(1, len(n)):
                if x < int(n[i]):
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
        else:
            for i in range(len(n)):
                if x > int(n[i]):
                    return n[:i] + str(x) + n[i:]
            return n + str(x)

test = Solution()
print test.maxValue("99", 9)
print test.maxValue("-13", 2)
print test.maxValue("-132", 3)