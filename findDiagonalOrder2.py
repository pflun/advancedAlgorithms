# -*- coding: utf-8 -*-
class Solution(object):
    def findDiagonalOrder2(self, nums):
        res = []
        dic = {}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                dic[i + j] = dic.get(i + j, []) + [nums[i][j]]
        for k, v in sorted(dic.items()):
            res.extend(v[::-1])
        return res

    # TLE, 10^5 * 10^5 = 10^10, 然而这是稀疏矩阵
    def findDiagonalOrder(self, nums):
        dic = {}
        res = []
        maxC = len(nums)
        maxR = 0
        for l in nums:
            maxR = max(maxR, len(l))
        for i in range(maxC):
            for j in range(maxR):
                if j >= len(nums[i]):
                    continue
                if i + j in dic:
                    dic[i + j].append(nums[i][j])
                else:
                    dic[i + j] = [nums[i][j]]
        # avoid sort dic
        for k in range(maxC + maxR - 1):
            if k in dic:
                res.extend(dic[k][::-1])
        return res

test = Solution()
print test.findDiagonalOrder2([[1,2,3],[4,5,6],[7,8,9]])
print test.findDiagonalOrder2([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]])
print test.findDiagonalOrder2([[1,2,3],[4],[5,6,7],[8],[9,10,11]])
print test.findDiagonalOrder2([[1,2,3,4,5,6]])
print test.findDiagonalOrder2([[6],[8],[6,1,6,16]])