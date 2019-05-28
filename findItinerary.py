# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def findItinerary(self, tickets):
        if len(tickets) == 0:
            return

        # get all node to node mapping
        import collections
        neighbors = collections.defaultdict(list)
        for u, v in tickets:
            neighbors[u].append(v)

        # graph = {}
        # for key, val in neighbors.items():
        #     graph[key] = DirectedGraphNode(key)
        #     graph[key].neighbors.append(val)
        #
        # countrd = collections.defaultdict(list)
        # for i in graph:
        #     print i
                # print j
                # countrd[j] = countrd[j] + 1


        return neighbors

test = Solution()
print test.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])