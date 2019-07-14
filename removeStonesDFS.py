class Solution(object):
    def removeStones(self, matrix):
        # grouped stones
        self.grouped = []
        # stone has been added (used) into grouped
        self.used = set()

        def dfs(matrix, visited, tmp, j, i):
            if j < 0 or j > len(matrix) - 1 or i < 0 or i > len(matrix[0]) - 1 or (j, i) in visited:
                return
            visited.add((j, i))
            tmp.append((j, i))
            self.used.add((j, i))
            # dfs on the same row
            for w in range(len(matrix[0])):
                if matrix[j][w] == 1:
                    dfs(matrix, visited, tmp, j, w)
            # dfs on the same col
            for h in range(len(matrix)):
                if matrix[h][i] == 1:
                    dfs(matrix, visited, tmp, h, i)
            return tmp

        for j in range(len(matrix)):
            for i in range(len(matrix[0])):
                if matrix[j][i] == 1 and (j, i) not in self.used:
                    group = dfs(matrix, set(), [], j, i)
                    self.grouped.append(group)

        removed = 0
        for g in self.grouped:
            removed += len(g)

        return removed - len(self.grouped), self.grouped

test = Solution()
print test.removeStones([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]])