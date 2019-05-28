from sortedArrayToBST import Solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def convertBST(self, root):
        self.values = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.values.append(root.val)
            inorder(root.right)

        inorder(root)
        offset = [0] * len(self.values)

        tmp = 0
        for i in range(len(self.values) - 1, -1, -1):
            tmp += self.values[i]
            offset[i] = tmp

        print offset
        vals = iter(offset)

        def inorder2(root):
            if not root:
                return
            inorder2(root.left)
            val = next(vals)
            # print root.val, val
            root.val = val
            inorder2(root.right)

        inorder2(root)
        return root

test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.convertBST(head_node).right.left.val

#    4
#  2   6
# 1 3 5 7
