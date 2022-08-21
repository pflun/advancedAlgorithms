class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        queue = graph[0]
        restricted = set(restricted)
        visited = set([0])
        res = 1 # node 0
        while queue:
            curr = queue.pop(0)
            if curr not in restricted and curr not in visited:
                res += 1
                visited.add(curr)
                if graph[curr]:
                    queue.extend(graph[curr])
        return res

test = Solution()
print test.reachableNodes(7, [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], [4,5])
print test.reachableNodes(7, [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], [4,2,1])
print test.reachableNodes(2, [[0,1]], [1])
