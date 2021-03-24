# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        if len(edges) != n - 1:
            return False

        import collections
        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        visited = {}
        from Queue import Queue
        queue = Queue()

        queue.put(0)
        visited[0] = True
        while not queue.empty():
            cur = queue.get()
            visited[cur] = True
            for node in neighbors[cur]:
                if node not in visited:
                    queue.put(node)

        print visited
        return len(visited) == n

test = Solution()
print test.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
print test.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])
print test.validTree(5, [[0,1],[1,2],[2,3],[1,3]])