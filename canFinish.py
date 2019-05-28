# -*- coding: utf-8 -*-
# Graph BFS + inDegree (Ru Du)
class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        inDegree = []
        dic = {}
        queue = []

        # Get Ru Du for each node
        for c in range(numCourses):
            inDegree.append(0)

        # pre_course => [courses]
        for prerequest in prerequisites:
            if prerequest[1] in dic:
                dic[prerequest[1]].append(prerequest[0])
            else:
                dic[prerequest[1]] = [prerequest[0]]

            # Calculate Ru Du for each node
            inDegree[prerequest[0]] += 1
        # print dic

        # Add Ru Du == 0 into Queue
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.pop(0)
            # get post courses and prepare to Ru Du -1
            subcourses = dic.get(course)

            # Last node won't have post courses (None), so need to exempt out None
            if subcourses == None:
                break

            # For each post course, Ru Du -1, add Ru Du == 0 node back to Queue
            for subcourse in subcourses:
                inDegree[subcourse] -= 1
                if inDegree[subcourse] == 0:
                    queue.append(subcourse)

        # Check if all Ru Du become 0 (0 means course can be took)
        if any(inDegree) != 0:
            return False
        return True

        # for key, value in dic.items():
        #     print key, value
        # print queue

# DFS Topological sort, 找环
# https://www.youtube.com/watch?v=M6SBePBMznU
class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
        visited = {}
        # 3 status: None (unknown), False (visiting), True (visited)
        # visiting means cycle found
        neighboors = {}

        # pre_course => [courses]
        for prerequest in prerequisites:
            if prerequest[1] in neighboors:
                neighboors[prerequest[1]].append(prerequest[0])
            else:
                neighboors[prerequest[1]] = [prerequest[0]]

        for i in range(numCourses):
            # not even touched
            if i not in visited:
                if self.dfs(i, visited, neighboors):
                    # found Cycle
                    return False

        return True

    def dfs(self, i, visited, neighboors):
        # visiting, found cycle
        if i in visited and not visited[i]:
            return True
        # visited, no cycle
        if i in visited and visited[i]:
            return False
        # set visiting
        visited[i] = False

        # make sure neighboor has the key
        if i in neighboors:
            # check neighboors
            for neighboor in neighboors[i]:
                if self.dfs(neighboor, visited, neighboors):
                    return True

        # after checking neighboors, set to visited
        visited[i] = True

        # no Cycle found
        return False

test = Solution()
print test.canFinish(3, [[1, 0], [2, 1], [2, 0]])