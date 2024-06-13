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

dic = {0: 0, 1: 9, 2: 8, 3: 7, 4: 6}
for k, v in sorted(dic.items(), key=lambda (k, v): (v, k)):
    print k, v
arr = [[1, 9], [2, 8], [3, 7], [4, 6]]
for a in sorted(arr, key=lambda x:x[1]):
    print a[0], a[1]
for k, v in sorted(dic.items(), reverse=True):
    print k, v
arr = ["cat", "bat", "rat"]
print " ".join(arr)
text = "aaa aaa"
print text.join("")