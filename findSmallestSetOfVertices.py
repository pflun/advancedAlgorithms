class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        indegree = []
        for i in range(n):
            indegree.append(0)
        for e in edges:
            indegree[e[1]] += 1
        res = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                res.append(i)
        return res

test = Solution()
print test.findSmallestSetOfVertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]])
print test.findSmallestSetOfVertices(5, [[0,1],[2,1],[3,1],[1,4],[2,4]])