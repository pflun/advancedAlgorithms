class Solution(object):
    # Bellman-Ford
    def maxProbability2(self, n, edges, succProb, start, end):
        self.dic = {}
        for i in range(len(edges)):
            a = edges[i][0]
            b = edges[i][1]
            p = succProb[i]
            self.dic[a] = self.dic.get(a, []) + [(b, p)]
            self.dic[b] = self.dic.get(b, []) + [(a, p)]
        probs = {}
        queue = [(start, 1)]
        while queue:
            parent, prob = queue.pop(0)
            if parent in self.dic:
                for next in self.dic[parent]:
                    nNode, nP = next
                    if nNode in probs:
                        # add to queue only if it can make better prob
                        if probs[nNode] > prob * nP:
                            continue
                    queue.append((nNode, prob * nP))
                    probs[nNode] = prob * nP
        return probs[end] if end in probs else 0

    # TLE at n = 5000
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
print test.maxProbability2(3, [[0,1],[1,2],[0,2]],[0.5,0.5,0.2], 0, 2)
print test.maxProbability2(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2)
print test.maxProbability2(3, [[0,1]], [0.5], 0, 2)