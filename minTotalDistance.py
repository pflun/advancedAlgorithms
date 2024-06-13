# https://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations-the-ell-1-norm?rq=1
# https://leetcode.com/problems/best-meeting-point/solutions/74196/python-solution-with-detailed-explanation/
class Solution(object):
    def minTotalDistance(self, grid):
        rows, cols = self.get_building_points(grid)
        x_median, y_median = self.get_median_co_ordinates(rows, cols)

        result = 0
        for x in rows:
            result += abs(x_median - x)
        for y in cols:
            result += abs(y_median - y)
        return result

    def get_building_points(self, grid):
        M, N = len(grid), len(grid[0])
        rows, cols = [], []
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        return rows, cols

    def get_median_co_ordinates(self, rows, cols):
        rows.sort()
        cols.sort()
        x_median, y_median = rows[len(rows) // 2], cols[len(cols) // 2]
        return x_median, y_median