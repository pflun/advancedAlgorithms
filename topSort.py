# Directed graph DFS
#
# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    def dfs(self, i, countrd, res):
        res.append(i)
        countrd[i] -= 1
        for j in i.neighbors:
            # delete edge, which is neighbor's Ru Du --
            countrd[j] = countrd[j] - 1
            # start dfs when neighbor's Ru Du == 0
            if countrd[j] == 0:
                self.dfs(j, countrd, res)
    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """
    def topSort(self, graph):
        # countrd means Ru Du for each node
        countrd = {}
        # add each node's Ru Du, use defaultdict seems better
        for x in graph:
            countrd[x] = 0

        # add if edge then Ru Du ++
        for i in graph:
            for j in i.neighbors:
                countrd[j] = countrd[j] + 1

        res = []
        # for each node, start dfs from node which Ru Du == 0
        for i in graph:
            if countrd[i] == 0:
                self.dfs(i, countrd, res)
        return res