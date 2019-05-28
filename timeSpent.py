# -*- coding: utf-8 -*-
# 水滴浸树
# 第一题，是一个台湾小姐姐，给了一颗树状图，每一个节点代表一个水塔，每一条边代表一根水管，每根水管上有一个数字，
# 代表水流过这个水管需要多久。问题是从root开始灌水，需要多久可以灌满整个图。follow up是如果图里有环该怎么做。
# 思路：
# 把树当成带权图，然后bfs或者dfs即可
class Node(object):
    def __init__(self, children, edge):
        self.children = children
        self.edge = edge

class Solution(object):
    def timeSpent(self, root):
        res = 0
        queue = [root]
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                res += curr.edge
                for child in curr.children:
                    queue.append(child)
        return res

n1 = Node([], 2)
n2 = Node([], 3)
root = Node([n1, n2], 0)
test = Solution()
print test.timeSpent(root)