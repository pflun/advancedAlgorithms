# -*- coding: utf-8 -*-
# https://www.cnblogs.com/grandyang/p/5282959.html
class Solution(object):
    # A/B里面有0不用算就直接跳过
    def multiply(self, A, B):
        res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for k in range(len(A[0])):
                if A[i][k] != 0:
                    for j in range(len(B[0])):
                        if B[k][j] != 0:
                            res[i][j] += A[i][k] * B[k][j]
        return res

    def multiplyBrutalForce(self, A, B):
        res = []
        for a in A:
            tmp = []
            for j in range(len(B[0])):
                col = []
                for i in range(len(B)):
                    col.append(B[i][j])
                curr = self.cal(a, col)
                tmp.append(curr)
            res.append(tmp)
        return res

    def cal(self, arr1, arr2):
        res = 0
        for i in range(len(arr1)):
            res += arr1[i] * arr2[i]
        return res

test = Solution()
print test.multiply([
  [ 1, 0, 0],
  [-1, 0, 3]
], [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
])
nums = [10,4,8,3]
print nums[len(nums):0:-1]