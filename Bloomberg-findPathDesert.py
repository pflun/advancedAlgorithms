# -*- coding: utf-8 -*-
# https://leetcode.com/discuss/interview-question/1608777/bloomberg-phone-screen-find-path-bw-2-objects-in-a-desert
# https://www.1point3acres.com/bbs/thread-967989-1-1.html
# Given a 2d matrix that represents a matrix where . denotes empty land, c indicates car, and o indicates oasis, and another integer gas which indicates gas we have left. Traversing one unit in the matrix consumes 1 gas unit. You can move up, down, left, and right.
# So Example: the matrix below and gas = 5 returns true since we can get from c to o in 5 units (1 unit left, 3 units down, and 1 unit right)
# [[. . . c .]
# [. . . . .]
# [. . . . .]
# [ . . o . .]]
#
# a) Check if car can reach oasis or not. (return bool val)
# b) Now suppose there is a gas station in the matrix somewhere that is denoted by an integer k where k represents the gas units that the car will be refuelled. So if k is 2, car will gain gas. Check if car can still reach oasis (with or without gas station).
# c) Now let's say there's obstacles in the matrix represented by r. how would you check if car can reach oasis? (Answered dfs with memoization)
class Solution(object):
    # a) and b) use manhattan distance, skip
    # c) BFS/DFS
    def findPathDesert(self, matrix, gas):
        queue = []
        for j in range(len(matrix)):
            for i in range(len(matrix[0])):
                if matrix[j][i] == 'c':
                    queue.append([j, i, gas])
                    break
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # y_x_gas because 3D state
        visited = set()
        while queue:
            curr = queue.pop()
            print curr
            for d in dir:
                curry = curr[0] + d[0]
                currx = curr[1] + d[1]
                currg = curr[2] - 1
                if curry < 0 or currx < 0 or curry > len(matrix) - 1 or currx > len(matrix[0]) - 1 or str(curry) + '_' + str(currx) + '_' + str(currg) in visited or matrix[curry][currx] == 'r' or currg < 0: # obstacles, currg<0 bc when currg=0, curry,currx can be target
                    continue
                if matrix[curry][currx].isdigit(): # gas station k
                    currg += int(matrix[curry][currx])
                if matrix[curry][currx] == 'o': # oasis
                    return True
                queue.append([curry, currx, currg])
                visited.add(str(curry) + '_' + str(currx) + '_' + str(currg))
        return False

test = Solution()
print test.findPathDesert([
    ['.', '.', '.', 'c', '.'],
    ['.', '.', '.', 'r', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '1', '.', '.'],
    ['.', '.', 'o', '.', '.']], 4) # 4 is enough to go to gas station, add 1 gas then go to oasis
