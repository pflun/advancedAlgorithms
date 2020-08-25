class Solution(object):
    def mostVisited(self, n, rounds):
        if rounds[0] <= rounds[-1]:
            return [x for x in range(rounds[0], rounds[-1] + 1)]
        else:
            return [x for x in range(1, rounds[-1] + 1)] + [x for x in range(rounds[0], n + 1)]

test = Solution()
print test.mostVisited(4, [1,3,1,2])
print test.mostVisited(2, [2,1,2,1,2,1,2,1,2])
print test.mostVisited(7, [1,3,5,7])