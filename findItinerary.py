# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

# Topological sort
class Solution(object):
    def findItinerary(self, tickets):
        if len(tickets) == 0:
            return

        self.res = []
        visited = {}
        # get all node to node mapping
        import collections
        neighbors = collections.defaultdict(list)
        for u, v in tickets:
            neighbors[u].append(v)

        for t in tickets:
            if t[0] not in visited:
                if self.dfs(t[0], visited, neighbors):
                    return False

        return self.res

    def dfs(self, city, visited, neighbors):
        # Cycle
        if city in visited and visited[city] == "visiting":
            return True
        elif city in visited and visited[city] == "visited":
            return False
        visited[city] = 'visiting'
        tmp = neighbors[city]
        for t in tmp:
            if self.dfs(t, visited, neighbors):
                return True
        visited[city] = 'visited'
        self.res = [city] + self.res
        return False

test = Solution()
print test.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])