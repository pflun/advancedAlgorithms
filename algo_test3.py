# -*- coding: utf-8 -*-
class Solution(object):
    # 静态变量
    TAG = "Person"
    def lexicographical(self, a, b):
        for i in range(5, -1, -1):
            print i

        matrix = [
                     [1, 5, 9],
                     [10, 11, 13],
                     [12, 13, 15]
                 ],
        res = matrix[0]
        for row in matrix[1:]:
            res.extend(row)

        changeTogether = [[float('-inf')] * 5] * 3
        changeTogether[0][0] = 1
        print changeTogether

        print Solution.TAG
        Solution2().printTwo()
        return a > b

    def isInteger(self, x):
        if type(x) == int:
            return True
        else:
            return False

    def trySet(self):
        res = []
        for num in set([1, 2, 2, 5, 5, 5]):
            res.append(num)
        print max([1, 2, 2, 5, 5, 5])
        return res

class Solution2(object):
    def printTwo(self):
        print '2'

class Solution3(object):
    def canFinish(self, prerequisites):
        neighboors = {}

        # pre_course => [courses]
        for prerequest in prerequisites:
            if prerequest[1] in neighboors:
                neighboors[prerequest[1]].append(prerequest[0])
            else:
                neighboors[prerequest[1]] = [prerequest[0]]

        for neighboor in neighboors[0]:
            print neighboor


# test = Solution()
# # print test.lexicographical('apple', 'appld')
# print test.trySet()

test = Solution3()
print test.canFinish([[1, 0], [2, 1], [2, 0]])