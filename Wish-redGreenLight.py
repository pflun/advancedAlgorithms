# -*- coding: utf-8 -*-
# 给了一个0/1数组，0代表绿灯，1代表红灯。反转一个区间的意思是说把这个区间里面的0变成1，1变成0，问经过一次反转最多能有多少个绿灯，然后反转区间的下标。
# 比如数组是[0,1,1,0,1,1] 可以反转下标 [1, 5]  这个区间，得到 [0,0,0,1,0,0]  这个最多五个绿灯的数组。返回[1, 5]即可（时间复杂度要求O(N)了）
# 我用二维dp做的，dp[i][j]代表从i到j进行翻转后绿灯的数量，其实就依赖dp[i][j - 1]
class Solution(object):
    def redGreenLight(self, arr):
        res = 0
        dp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
        defaultGreen = self.getGreen(arr)
        for i in range(len(arr)):
            if arr[i] == 0:
                curr = defaultGreen - 1
            else:
                curr = defaultGreen + 1
            dp[i][i] = curr
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] == 0:
                    dp[i][j] = dp[i][j - 1] - 1
                else:
                    dp[i][j] = dp[i][j - 1] + 1
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                res = max(res, dp[i][j])
        return res

    def getGreen(self, arr):
        cnt = 0
        for a in arr:
            if a == 0:
                cnt += 1
        return cnt

test = Solution()
print test.redGreenLight([0,1,1,0,1,1])