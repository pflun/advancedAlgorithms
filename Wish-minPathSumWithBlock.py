class Solution(object):
    def minPathSum(self, grid):
        prev = [float('inf') for _ in range(len(grid[0]))]
        curr = [float('inf') for _ in range(len(grid[0]))]
        # initialize
        prev[0] = grid[0][0]
        for i in range(1, len(grid[0])):
            prev[i] = prev[i - 1] + grid[0][i] if grid[0][i] != '#' else float('inf')

        for j in range(1, len(grid)):
            curr[0] = prev[0] + grid[j][0] if grid[j][0] != '#' else float('inf')
            for i in range(1, len(grid[0])):
                if grid[j][i] == '#':
                    curr[i] = float('inf')
                else:
                    curr[i] = min(curr[i - 1], prev[i]) + grid[j][i]
            prev = curr

        return curr[-1]

test = Solution()
print test.minPathSum([
  [1,3,'#'],
  [1,5,1],
  [4,2,1]
])