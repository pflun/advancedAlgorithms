# -*- coding: utf-8 -*-
class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        robots = []
        for i in range(len(positions)):
            robots.append([positions[i], healths[i], directions[i]])
        robots.sort()
        stack = []
        # assume everyone move to right, if someone move to left it will collide
        for i in range(len(robots)):
            # 1. stack empty无论如何append, 2. stack顶端向左 <= 和 => 不会collide, 3. 向右不会collide
            if not stack or stack[-1][2] == "L" or robots[i][2] == "R":
                stack.append(robots[i])
            # collide
            else:
                # 可以collide
                while stack and stack[-1][2] == "R":
                    if stack[-1][1] > robots[i][1]:
                        stack[-1][1] -= 1
                        robots[i][1] = 0
                        if stack[-1][1] == 0:
                            stack.pop()
                        break
                    elif stack[-1][1] < robots[i][1]:
                        stack.pop()
                        robots[i][1] -= 1
                    else:
                        stack.pop()
                        robots[i][1] = 0
                        break
                    if robots[i][1] > 0:
                        stack.append(robots[i])
        # 其实到这里这道题就结束了，stack已经找到最后剩下的robots
        # 但是这题要求 return original input order, 1. 写个comparator按初始input给stack重新排序
        # 或者 2. 减health而不是stack[i][1]，forloop找health > 0的robot 免得重新排序
        # 2参考: https://leetcode.com/problems/robot-collisions/solutions/3679168/java-c-python-stack-soluton/
        # position (相当于id了) => input index 这也就是original order
        dic = {}
        for i in range(len(positions)):
            dic[positions[i]] = i

        # custom comparator, 按照 -1, 0, 1 排序
        def compare(a, b):
            if dic[a[0]] < dic[b[0]]:
                # 小的排在前
                return -1
            elif dic[a[0]] > dic[b[0]]:
                # 大的排在后
                return 1
            return 0

        sorted_stack = sorted(stack, cmp=lambda a, b: compare(a, b))
        res = []
        for robot in sorted_stack:
            res.append(robot[1])
        return res

test = Solution()
print test.survivedRobotsHealths([5,4,3,2,1], [2,17,9,15,10], "RRRRR")
print test.survivedRobotsHealths([3,5,2,6], [10,10,15,12], "RLRL")
print test.survivedRobotsHealths([1,2,5,6], [10,10,11,11], "RLRL")
print test.survivedRobotsHealths([2], [2], "L")
print test.survivedRobotsHealths([3,40], [49,11], "LL")
# Bug, expected: [18], output: [1,19]
print test.survivedRobotsHealths([11,44,16], [1,20,17], "RLR")