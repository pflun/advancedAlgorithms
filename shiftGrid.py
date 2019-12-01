class Solution(object):
    def shiftGrid(self, grid, k):
        for _ in range(k):
            last = []
            for i in range(len(grid)):
                last.append(grid[i][len(grid[0]) - 1])
            last = [last[-1]] + last[:-1]
            for i in range(len(grid)):
                for j in range(len(grid[0]) - 1, 0, -1):
                    grid[i][j] = grid[i][j - 1]
            for i in range(len(last)):
                grid[i][0] = last[i]
        return grid

test = Solution()
print test.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1)
print test.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4)
print test.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 9)