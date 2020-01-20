# -*- coding: utf-8 -*-
import copy
class Solution(object):
    def test(self):
        res = []
        matrix = [[0,0],[0,0]]
        m1 = self.helper(copy.deepcopy(matrix))
        print m1
        res.append(m1)
        m2 = self.helper(copy.deepcopy(matrix))
        print m2
        res.append(m2)
        print res

    def helper(self, matrix):
        if matrix[0][0] == 0:
            matrix[0][0] = 1
        else:
            matrix[0][0] = 0
        return matrix

test = Solution()
test.test()