class Solution(object):
    def addToArrayForm(self, A, K):
        intA = 0
        pos = 1
        for a in reversed(A):
            intA += a * pos
            pos *= 10

        return [int(x) for x in str(intA + K)]

test = Solution()
print test.addToArrayForm([2,7,4], 181)