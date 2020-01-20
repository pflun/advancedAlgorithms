import copy
class Solution(object):
    def minFlips(self, mat):
        queue = [mat]
        visited = set()
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                for i in range(len(curr)):
                    for j in range(len(curr[0])):
                        newCurr = self.flip(copy.deepcopy(curr), i, j)
                        if self.serialize(newCurr) in visited:
                            continue
                        if self.valid(newCurr):
                            return step + 1
                        visited.add(self.serialize(newCurr))
                        queue.append(newCurr)
            step += 1
        return -1

    def flip(self, matrix, i, j):
        for y in range(len(matrix[0])):
            if matrix[i][y] == 0:
                matrix[i][y] = 1
            else:
                matrix[i][y] = 0
        for x in range(len(matrix)):
            if matrix[x][j] == 0:
                matrix[x][j] = 1
            else:
                matrix[x][j] = 0
        if matrix[i][j] == 0:
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0
        return matrix

    def valid(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    return False
        return True

    def serialize(self, matrix):
        res = ''
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res += str(matrix[i][j]) + '_'
        return res

test = Solution()
print test.minFlips([[0,0],[0,1]])
print test.minFlips([[1,1,1],[1,0,1],[0,0,0]])
print test.minFlips([[1,0,0],[1,0,0]])