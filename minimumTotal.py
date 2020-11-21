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

    def minimumTotal2(self, triangle):
        dp = [triangle[0]]
        for i in range(1, len(triangle)):
            tmp = []
            for j in range(len(triangle[i])):
                if j == 0:
                    tmp.append(dp[i - 1][0] + triangle[i][0])
                elif j == len(triangle[i]) - 1:
                    tmp.append(dp[i - 1][-1] + triangle[i][-1])
                else:
                    tmp.append(min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j])
            dp.append(tmp)
        return min(dp[-1])

test = Solution()
print test.minimumTotal2([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])