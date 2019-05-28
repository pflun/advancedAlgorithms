# https://leetcode.com/problems/pascals-triangle/description/
class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        
        res = [[1], [1, 1]]
        for row in range(2, numRows):
            level = [1]
            for i in range(1, row):
                tmp = res[row - 1][i - 1] + res[row - 1][i]
                level.append(tmp)
            level.append(1)
            res.append(level)

        return res

test = Solution()
print test.generate(5)