class Solution(object):
    def getLastMoment(self, n, left, right):
        if len(left) != 0:
            leftMost = max(left)
        else:
            leftMost = 0
        if len(right) != 0:
            rightMost = min(right)
        else:
            rightMost = n
        return max(n - rightMost, leftMost)

test = Solution()
print test.getLastMoment(4, [4,3], [0,1])
print test.getLastMoment(7, [], [0,1,2,3,4,5,6,7])
print test.getLastMoment(7, [0,1,2,3,4,5,6,7], [])
print test.getLastMoment(9, [5], [4])
print test.getLastMoment(6, [6], [0])
