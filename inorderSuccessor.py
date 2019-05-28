from sortedArrayToBST import Solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def inorderSuccessor(self, root, p):
        # Global variables
        # Record prev visited node everytime
        self.prev = None
        self.res = None

        def inorder(root):
            if root is None:
                return None
            inorder(root.left)
            # If prev == p that means current node is the successor
            if self.prev == p:
                self.res = root.val
            else:
                # move prev one step forward to current
                self.prev = root.val

            inorder(root.right)

        inorder(root)

        return self.res

test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.inorderSuccessor(head_node, 6)

#    4
#  2   6
# 1 3 5 7