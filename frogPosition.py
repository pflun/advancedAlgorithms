class Solution(object):
    def frogPosition(self, n, edges, t, target):
        graph = {}
        for e in edges:
            fm = e[0]
            to = e[1]
            if fm not in graph:
                graph[fm] = [to]
            else:
                graph[fm].append(to)
        self.prob = 0
        self.found = False
        def dfs(graph, next, t, prob, target):
            if self.found:
                return
            if t == 0 and next == target:
                # print prob
                self.prob = 1 / float(prob)
                self.found = True
            elif next == target:
                self.prob = 1 / float(prob)
                self.found = True
            if next not in graph:
                return
            curr = graph[next]
            for c in curr:
                dfs(graph, c, t - 1, prob * len(curr), target)
        dfs(graph, 1, t, 1, target)
        return self.prob

test = Solution()
print test.frogPosition(7,[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]],2,4)
print test.frogPosition(7,[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]],1,7)
print test.frogPosition(7,[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]],20,6)