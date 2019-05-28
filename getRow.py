class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        res = [[1], [1, 1]]
        for row in range(2, rowIndex + 1):
            level = [1]
            for i in range(1, row):
                tmp = res[row - 1][i - 1] + res[row - 1][i]
                level.append(tmp)
            level.append(1)
            res.append(level)

        return res[rowIndex]

test = Solution()
print test.getRow(2)