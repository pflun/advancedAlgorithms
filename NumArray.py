# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=awS9dn_XCmI
class NumArray(object):
    def __init__(self, nums):

        # Tip: generate all 0 matrix
        self.matrix = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

        # self.matrix[i][j] stand for Sum from nums[i] to nums[j]
        # maybe MLE
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                tmp = 0
                for k in range(i, j + 1):
                    tmp += nums[k]
                self.matrix[i][j] = tmp

    def sumRange(self, i, j):

        return self.matrix[i][j]

class NumArray2(object):
    def __init__(self, nums):

        self.res = [0 for _ in range(len(nums))]

        # self.res[i][j] : nums[0] + nums[1] + ...... + nums[i]
        # 进一步优化DP: self.res[i] = self.res[i - 1] + nums[i]
        for i in range(len(nums)):
            tmp = 0
            for k in range(0, i + 1):
                tmp += nums[k]
            self.res[i] = tmp


    def sumRange(self, i, j):

        if i == 0:
            return self.res[j]

        # [2, 5] 就是前5个元素和减去前1个元素和
        return self.res[j] - self.res[i - 1]



obj = NumArray2([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0, 5)
print param_1