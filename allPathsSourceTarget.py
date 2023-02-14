class Solution(object):
    def allPathsSourceTarget(self, graph):
        self.res = []
        self.dic = {}
        for i in range(len(graph)):
            self.dic[i] = self.dic.get(i, []) + graph[i]

        def dfs(curr, dest, path):
            if curr == dest:
                # deep copy!
                self.res.append(path[:])
                return
            for neighbor in self.dic[curr]:
                path.append(neighbor)
                dfs(neighbor, dest, path)
                path.pop()

        dfs(0, len(graph) - 1, [0])
        return self.res


test = Solution()
print test.allPathsSourceTarget([[1,2],[3],[3],[]])
print test.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])