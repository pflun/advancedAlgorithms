class Solution(object):
    # bug
    def unhappyFriends(self, n, preferences, pairs):
        self.dic = {}
        for p in pairs:
            self.dic[p[0]] = p[1]
            self.dic[p[1]] = p[0]
        res = 0
        for p in pairs:
            if self.unhappy(preferences, p[0], p[1]):
                res += 1
            elif self.unhappy(preferences, p[1], p[0]):
                res += 1
        return res

    def unhappy(self, preferences, x, y):
        xList = preferences[x]
        for a in xList:
            if a == y:
                return False
            aList = preferences[a]
            aShouldPair = self.dic[a]
            try:
                xPos = aList.index(x)
            except:
                xPos = 501
            try:
                aShouldPairPos = aList.index(aShouldPair)
            except:
                aShouldPairPos = 501
            if xPos < aShouldPairPos:
                return True

        return False

test = Solution()
print test.unhappyFriends(4, [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], [[0, 1], [2, 3]])
print test.unhappyFriends(2, [[1], [0]], [[1, 0]])
print test.unhappyFriends(4, [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], [[1, 3], [0, 2]])