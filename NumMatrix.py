class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)
        if matrix is None or not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        self.sum = []
        self.res = 0

        # generate all zeros matrix
        for i in range(m + 1):
            tmp = []
            for j in range(n + 1):
                tmp.append(0)
            self.sum.append(tmp)

        # preprocess
        # sum: a rectangle from [0, 0] to [i, j]'s sum val (in this case, how many 1s in this area)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.sum[i][j] = int(matrix[i - 1][j - 1]) + self.sum[i - 1][j] + self.sum[i][j - 1] - self.sum[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        self.res = self.sum[row2 + 1][col2 + 1] - self.sum[row1][col2 + 1] - self.sum[row2 + 1][col1] + self.sum[row1][col1]

        return self.res

obj = NumMatrix([[3,0,1,4,2],
                 [5,6,3,2,1],
                 [1,2,0,1,5],
                 [4,1,0,1,7],
                 [1,0,3,0,5]])
param_1 = obj.sumRegion(2,1,4,3)
print param_1