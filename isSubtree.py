# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        res = []
        queue = [s]

        while queue:
            curr = queue.pop(0)
            if self.helper(curr, t):
                res.append(True)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return any(res)


    def helper(self, s, t):
        if not s and not t:
            return True
        elif s and not t:
            return True
        elif t and not s:
            return False
        elif t and s:
            if s.val == t.val:
                return self.helper(s.left, t.left) and self.helper(s.right, t.right)
            else:
                return False


head_node = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(0)
n3 = TreeNode(5)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(5)
n7 = TreeNode(5)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
n3.left = n6
n6.left = n5
n6.right = n7

head_node2 = TreeNode(5)
m1 = TreeNode(5)
m2 = TreeNode(5)
head_node2.left = m1
head_node2.right = m2

test = Solution()
print test.isSubtree(head_node, head_node2)

#     0
#   1   0
#  5 4
# 5
#5 5