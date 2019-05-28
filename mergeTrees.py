# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        if t1 and not t2:
            return t1
        elif not t1 and t2:
            return t2

        def helper(t1, t2):
            if not t1 and not t2:
                return None
            if t1 and not t2:
                return t1
            if not t1 and t2:
                return t2
            if t1 and t2:
                t1.val += t2.val

            t1.left = helper(t1.left, t2.left)
            t1.right = helper(t1.right, t2.right)

            return t1

        helper(t1, t2)

        return t1

head_node = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(5)
n3 = TreeNode(2)
n4 = TreeNode(4)
n5 = TreeNode(3)
n6 = TreeNode(6)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
n3.left = n5
n5.right = n6

head_node2 = TreeNode(10)
m1 = TreeNode(1)
m2 = TreeNode(2)
m3 = TreeNode(3)
head_node2.left = m1
head_node2.right = m2
m2.right = m3

test = Solution()
print test.mergeTrees(head_node, head_node2).right.right.val

#     0
#   1   5
#  2 4
# 3
#  6