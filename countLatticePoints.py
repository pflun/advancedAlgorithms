class Solution(object):
    def countLatticePoints(self, circles):
        res = set()
        for c in circles:
            x = c[0]
            y = c[1]
            r = c[2]
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if abs(i - x) ** 2 + abs(j - y) ** 2 <= r ** 2:
                        res.add((i, j))
        return len(res)

test = Solution()
print test.countLatticePoints([[2,2,1]])
print test.countLatticePoints([[2,2,2],[3,4,1]])