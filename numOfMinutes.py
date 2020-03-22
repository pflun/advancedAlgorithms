class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        graph = {}
        graph[headID] = []
        for i in range(len(manager)):
            if manager[i] in graph:
                graph[manager[i]].append(i)
            else:
                graph[manager[i]] = [i]
        self.res = 0
        def dfs(graph, next, tmpT, informTime):
            if next not in graph:
                self.res = max(self.res, tmpT)
                return
            sub = graph[next]
            for s in sub:
                dfs(graph, s, tmpT + informTime[next], informTime)

        dfs(graph, headID, 0, informTime)
        return self.res

test = Solution()
print test.numOfMinutes(1,0,[-1],[0])
print test.numOfMinutes(6,2,[2,2,-1,2,2,2],[0,0,1,0,0,0])
print test.numOfMinutes(7,6,[1,2,3,4,5,6,-1],[0,6,5,4,3,2,1])
print test.numOfMinutes(15,0,[-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6],[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])
print test.numOfMinutes(4,2,[3,3,-1,2],[0,0,162,914])