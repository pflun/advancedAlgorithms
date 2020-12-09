import heapq
# Another post order traversal solution: https://leetcode.com/problems/reconstruct-itinerary/discuss/437594/super-easy-and-clean-Javascript-(Greedy)-DFS-with-detailed-explanations
# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def findItinerary2(self, tickets):
        self.res = []
        # departure => <heap> arrivals
        self.dic = {}
        for t in tickets:
            if t[0] not in self.dic:
                heap = []
                heapq.heapify(heap)
                heapq.heappush(heap, t[1])
                self.dic[t[0]] = heap
            else:
                heapq.heappush(self.dic[t[0]], t[1])
        self.dfs2('JFK')
        return self.res

    def dfs2(self, departure):
        if departure not in self.dic:
            self.res = [departure] + self.res
            return
        heap = self.dic[departure]
        while heap:
            self.dfs2(heapq.heappop(heap))
        self.res = [departure] + self.res

    # Topological sort
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
print test.findItinerary2([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])