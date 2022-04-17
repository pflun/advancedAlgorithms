# Correct (code is wrong)
# The basic idea is to do BFS and adding children from the opposite color for the curr explored node. This will ensure only the valid paths are added to q (we add <node#, incoming-edge-color-to-node> to q).
# So there is not need to keep track of valid paths or their lengths.
# The tricky part is to figure out avoiding loops in the BFS. Simply, skipping the visited nodes will also skip other valid paths. But if we do not skip visited nodes, obviously cycles will be a problem.
class Solution(object):
    # compile bug
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        red = [float('inf') for _ in range(n)]
        blue = [float('inf') for _ in range(n)]
        red[0] = 0
        blue[0] = 0
        red_graph = {}
        blue_graph = {}
        for r in red_edges:
            red_graph[r[1]] = red_graph.get(r[1], []) + [r[0]]
        for r in blue_edges:
            blue_graph[r[1]] = blue_graph.get(r[1], []) + [r[0]]
        for i in range(1, n):
            parents_red = red_graph[i]
            tmp = float('inf')
            for p in parents_red:
                tmp = min(tmp, red[p])
            if tmp != float('inf'):
                blue[i] = tmp + 1
            parents_blue = blue_graph[i]
            tmp = float('inf')
            for p in parents_blue:
                tmp = min(tmp, blue[p])
            if tmp != float('inf'):
                red[i] = tmp + 1
        res = [min(red[i], blue[i]) for i in range(n)]
        return res

test = Solution()
print test.shortestAlternatingPaths(3, [[0,1],[1,2]], [])
print test.shortestAlternatingPaths(3, [[0,1]], [[2,1]])
print test.shortestAlternatingPaths(3, [[1,0]], [[2,1]])