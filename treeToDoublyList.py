from sortedArrayToBST import Solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def treeToDoublyList(self, root):
        dummy = TreeNode(0)
        # Tip: self.prev is the global variable used for previous visted node
        self.prev = dummy

        def inorder(root):
            if root is None:
                return None
            inorder(root.left)
            # left point to previous visted node
            root.left = self.prev
            # previous visted node's right point to current
            self.prev.right = root
            # previous move one step to current (will become prev for next circle)
            self.prev = root
            inorder(root.right)

        inorder(root)

        # traverse = head
        traverse = dummy.right
        # go to last node (tip: go to second last then traverse = traverse.right)
        while traverse.right != None:
            traverse = traverse.right
        # doubly link head and last node
        traverse.right = dummy.right
        dummy.right.left = traverse

        return dummy.right

test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.treeToDoublyList(head_node).right.right.right.right.right.right.left.val

#    4
#  2   6
# 1 3 5 7