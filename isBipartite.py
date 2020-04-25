# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=NOddgU7AZxc
# 给每一个node上色，比如当前上白色，邻居就上黑色。能不能根据这个逻辑全部上色
# 0没上色 1白色 -1黑色
class Solution(object):
    def isBipartite(self, graph):
        colors = [0 for _ in range(len(graph))]
        for i in range(len(graph)):
            # 没上色，涂不上色
            if colors[i] == 0 and not dfs(graph, colors, 1, i):
                return False
        return True

    def dfs(self, graph, colors, color, i):
        # 已经有色
        if colors[i] != 0:
            return True if colors[i] == color else False
        colors[i] = color
        # 涂邻居
        for n in graph[i]:
            # 邻居涂色不成功，直接false
            if not dfs(graph, colors, -color, n):
                return False
        return True