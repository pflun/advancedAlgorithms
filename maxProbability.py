class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        self.res = 0
        self.dic = {}
        for i in range(len(edges)):
            a = edges[i][0]
            b = edges[i][1]
            p = succProb[i]
            self.dic[a] = self.dic.get(a, []) + [(b, p)]
            self.dic[b] = self.dic.get(b, []) + [(a, p)]

        def dfs(currNode, currP, end, visited):
            if currNode in visited:
                return
            # pruning
            if currP <= self.res:
                return
            visited.add(currNode)
            if currNode == end:
                self.res = max(self.res, currP)
            if currNode in self.dic:
                next = self.dic[currNode]
                for n in next:
                    nNode, nP = n
                    dfs(nNode, currP * nP, end, visited)
                visited.remove(currNode)

        dfs(start, 1, end, set())
        return self.res

test = Solution()
print test.maxProbability(3, [[0,1],[1,2],[0,2]],[0.5,0.5,0.2], 0, 2)
print test.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2)
print test.maxProbability(3, [[0,1]], [0.5], 0, 2)