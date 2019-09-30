# -*- coding: utf-8 -*-
# 反对角线 x + y 等于定值，boolean决定正着加还是反着加
class Solution(object):
    def findDiagonalOrder(self, matrix):
        dic = {}
        res = []
        flag = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i + j in dic:
                    dic[i + j].append(matrix[i][j])
                else:
                    dic[i + j] = [matrix[i][j]]
        for k, v in sorted(dic.items()):
            if flag == 0:
                res.extend(v[::-1])
                flag = 1
            else:
                res.extend(v)
                flag = 0

        return res

test = Solution()
print test.findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])