class Solution(object):
    def unhappyFriends2(self, n, preferences, pairs):
        prefer = {}
        pair = {}
        for p1, p2 in pairs:
            pair[p1] = p2
            pair[p2] = p1
        for i in range(len(preferences)):
            for j in range(len(preferences[i])):
                if i not in prefer:
                    prefer[i] = {}
                # {person_1 => {person_2 : order}}
                prefer[i][preferences[i][j]] = j
        res = 0
        for i in range(len(preferences)):
            for j in range(len(preferences[i])):
                x = i
                y = pair[x]
                u = preferences[x][j]  # for all x's preferences
                v = pair[u]
                if prefer[x][u] < prefer[x][y] and prefer[u][x] < prefer[u][v]:
                    res += 1
                    break
        return res

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