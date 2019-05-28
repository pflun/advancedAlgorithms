# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        if not root:
            return None
        if d < 1:
            return root
        elif d == 1:
            d1Node = TreeNode(v)
            d1Node.left = root
            return d1Node
        queue = [(root, 1)]

        while queue:
            for _ in range(len(queue)):
                curr, level = queue.pop(0)
                if level == d - 1:
                    if curr.left:
                        leftNode = TreeNode(v)
                        leftNode.left = curr.left
                        curr.left = leftNode
                    else:
                        leftNode = TreeNode(v)
                        curr.left = leftNode
                    if curr.right:
                        rightNode = TreeNode(v)
                        rightNode.right = curr.right
                        curr.right = rightNode
                    else:
                        rightNode = TreeNode(v)
                        curr.right = rightNode

                if curr.left:
                    queue.append((curr.left, level + 1))
                if curr.right:
                    queue.append((curr.right, level + 1))

        return root

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
print test.addOneRow(head_node, 9, 2).right.val

#     0
#   1   2
#  3 4
# 5
#6 7