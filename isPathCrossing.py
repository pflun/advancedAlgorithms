class Solution(object):
    def isPathCrossing(self, path):
        visited = set()
        visited.add((0, 0))
        x = 0
        y = 0
        for p in path:
            if p == 'N':
                y += 1
            elif p == 'S':
                y -= 1
            elif p == 'E':
                x += 1
            elif p == 'W':
                x -= 1
            tmp = (x, y)
            if tmp in visited:
                return True
            else:
                visited.add(tmp)
        return False

test = Solution()
# print test.isPathCrossing("NES")
# print test.isPathCrossing("NESWW")
# print test.isPathCrossing("SN")
print test.isPathCrossing("W")