class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0:
            return matrix

        res = []
        for _ in range(len(matrix)):
            tmp = []
            for _ in range(len(matrix[0])):
                tmp.append(0)
            res.append(tmp)

        for i in range(len(res)):
            for j in range(len(res[0])):
                if matrix[i][j] != 0:
                    cell = self.bfs(matrix, i, j)
                    res[i][j] = cell

        return res

    def bfs(self, matrix, x, y):
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set((x, y))
        queue = [[x, y]]
        counter = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop()
                for d in dir:
                    currx = curr[0] + d[0]
                    curry = curr[1] + d[1]
                    if currx < 0 or currx == len(matrix) or curry < 0 or curry == len(matrix[0]) or (
                    currx, curry) in visited:
                        continue
                    if matrix[currx][curry] == 0:
                        return counter
                    visited.add((currx, curry))
                    queue.append([currx, curry])

            counter += 1

        return -1

test = Solution()
print test.updateMatrix([
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]])


def isAnagram(s, t):

    if len(s) != len(t):
        return False
    elif len(s) == 0 and len(t) == 0:
        return True

    return sorted(s) == sorted(t)

print isAnagram("anagram", "nagaram")

odd = False
# odd = not odd
print odd
