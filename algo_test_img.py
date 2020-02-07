class Solution(object):
    # 2 dimensional
    def test2D(self, input):
        res = [[0 for _ in range(len(input[0]) * 2)] for _ in range(len(input) * 2)]
        offsetx = 0
        for i in range(len(input)):
            offsety = 0
            for j in range(len(input[0])):
                res[i + offsetx][j + offsety] = input[i][j]
                offsety += 1
            offsetx += 1
        return res

    # 2 dimensional
    def test3D(self, input):
        res = [[[0 for _ in range(len(input[0][0]) * 2)] for _ in range(len(input[0]) * 2)] for _ in range(len(input) * 2)]
        offsetx = 0
        for i in range(len(input)):
            offsety = 0
            for j in range(len(input[0])):
                offsetz = 0
                for k in range(len(input[0][0])):
                    res[i + offsetx][j + offsety][k + offsetz] = input[i][j][k]
                    offsetz += 1
                offsety += 1
            offsetx += 1
        return res

test = Solution()
print test.test2D([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print test.test3D([
    [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ],
    [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ],
    [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ],
])