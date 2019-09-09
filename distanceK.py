# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        self.res = []
        self.visited = set()
        graph = {}

        def traverse(node):
            if node.left:
                if node.val in graph:
                    graph[node.val].append(node.left.val)
                else:
                    graph[node.val] = [node.left.val]
                if node.left.val in graph:
                    graph[node.left.val].append(node.val)
                else:
                    graph[node.left.val] = [node.val]
                traverse(node.left)
            if node.right:
                if node.val in graph:
                    graph[node.val].append(node.right.val)
                else:
                    graph[node.val] = [node.right.val]
                if node.right.val in graph:
                    graph[node.right.val].append(node.val)
                else:
                    graph[node.right.val] = [node.val]
                traverse(node.right)

        traverse(root)

        def dfs(curr, distance):
            if curr in self.visited:
                return
            self.visited.add(curr)
            if distance == 0:
                self.res.append(curr)
                return
            for c in graph[curr]:
                dfs(c, distance - 1)

        dfs(target.val, K)
        return self.res

head_node = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
n3.left = n5
n5.left = n6
n5.right = n7

test = Solution()
print test.distanceK(head_node, n3, 2)

#     0
#   1   2
#  3 4
# 5
#6 7