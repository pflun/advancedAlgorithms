class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        if not triangle:
            return
        # bottom to top, everytime update upper level node with self + min(son.left, son.right)
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
            print triangle[i]
        return triangle[0][0]

test = Solution()
print test.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])