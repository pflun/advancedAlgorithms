class Solution(object):
    def minKnightMoves(self, x, y):
        dir = [[1, 2], [2, 1], [-1, 2], [2, -1], [1, -2], [-2, 1], [-1, -2], [-2, -1]]
        visited = set()
        queue = [[0, 0]]
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                visited.add(self.hash(curr[0], curr[1]))
                if curr == [x, y]:
                    return step
                for d in dir:
                    nx = curr[0] + d[0]
                    ny = curr[1] + d[1]
                    if self.hash(nx, ny) not in visited:
                        queue.append([nx, ny])
            step += 1

        return -1

    def hash(self, x, y):
        return str(x) + '_' + str(y)

test = Solution()
print test.minKnightMoves(2, 1)
print test.minKnightMoves(5, 5)