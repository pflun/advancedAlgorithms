class Solution(object):
    def findTheWinner(self, n, k):
        friends = [i for i in range(1, n + 1)]
        idx = 0
        while len(friends) > 1:
            idx = (idx + k - 1) % len(friends)
            friends = friends[:idx] + friends[idx + 1:]
        return friends[0]

test = Solution()
print test.findTheWinner(5, 2)
print test.findTheWinner(6, 5)