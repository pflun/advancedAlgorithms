# -*- coding: utf-8 -*-
# 起点0， 重点2
class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        dic = {}
        queue = []

        # pre_course => [courses]
        for prerequest in prerequisites:
            if prerequest[1] in dic:
                dic[prerequest[1]].append(prerequest[0])
            else:
                dic[prerequest[1]] = [prerequest[0]]
        print dic
        # 起点，比如是0（所以append 0）
        queue.append(0)

        while queue:
            course = queue.pop(0)
            # get post courses and prepare to Ru Du -1
            subcourses = dic.get(course)

            # Last node won't have post courses (None), so need to exempt out None
            if subcourses == None:
                break

            # For each post course, Ru Du -1, add Ru Du == 0 node back to Queue
            for subcourse in subcourses:
                # 终点 2的话结果是True，终点 3 结果False
                if subcourse == 3:
                    return True
                queue.append(subcourse)

        return False

test = Solution()
print test.canFinish(3, [[1, 0], [2, 1], [2, 0]])