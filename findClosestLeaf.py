# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=x1wXkRrpavw
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findClosestLeaf(self, root, k):
        self.start = None
        self.graph = {}

        # DFS建图，找出起始点k
        def buildGraph(node, parent, k):
            if not node:
                return
            if node.val == k:
                self.start = node

            # 对称加邻居，child => [parent], parent => [child]
            if parent:
                if node not in self.graph:
                    self.graph[node] = [parent]
                else:
                    self.graph[node].append(parent)
                if parent not in self.graph:
                    self.graph[parent] = [node]
                else:
                    self.graph[parent].append(node)

            buildGraph(node.left, node, k)
            buildGraph(node.right, node, k)

        buildGraph(root, None, k)

        # 避免死循环
        visited = set()
        queue = [self.start]

        # BFS 按层
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                visited.add(curr)
                # found leaf
                if not curr.left and not curr.right:
                    return curr
                for neighbor in self.graph[curr]:
                    # 没有访问过
                    if neighbor not in visited:
                        queue.append(neighbor)

        # 最终一定会找到的，所以无所谓return
        return 0

head_node = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
head_node.left = n1
head_node.right = n2
n1.left = n3
n3.left = n6
n6.left = n5
n6.right = n7

test1 = Solution()
print test1.findClosestLeaf(head_node, 1).val

#     0
#   1   2
#  3
# 6
#5 7