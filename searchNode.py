# Given a undirected graph, a node and a target, return the nearest node to given node which value of it is target, return NULL if you can't find.
# 2------3  5
#  \     |  |
#   \    |  |
#    \   |  |
#     \  |  |
#       1 --4
# Give a node 1, target is 50
#
# there a hash named values which is [3,4,10,50,50]

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def searchNode(self, edges, values, target):

        if len(edges) == 0 or len(values) == 0:
            return

        # get all node to node mapping
        import collections
        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        visited = {}
        hash_value = {}
        i = 1
        for hv in values:
            hash_value[i] = hv
            i += 1

        from Queue import Queue
        queue = Queue()

        queue.put(1)
        visited[1] = True
        while not queue.empty():
            cur = queue.get()
            visited[cur] = True
            if hash_value[cur] == target:
                return cur
            for node in neighbors[cur]:
                # add not visited neighbors into queue
                if node not in visited:
                    queue.put(node)

test = Solution()
print test.searchNode([[1, 2], [2, 3], [1, 3], [1, 4], [4, 5]], [3, 4, 10, 50, 50], 50)