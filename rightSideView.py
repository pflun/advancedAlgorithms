from sortedArrayToBST import Solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def rightSideView(self, root):
        if root is None:
            return []
        stack = [(root, 0)]
        dic = {}
        res = []

        while stack:
            node, level = stack.pop()
            dic[level] = node.val

            if node.right:
                stack.append((node.right, level + 1))

            if node.left:
                stack.append((node.left, level + 1))

        for key, value in dic.items():
            res.append(value)

        return res

    def rightSideView2(self, root):
        if root is None:
            return []

        dic = {}
        res = []

        def inorder(root, dic, level):
            if not root:
                return None

            if root.left:
                inorder(root.left, dic, level + 1)

            dic[level] = root.val

            if root.right:
                inorder(root.right, dic, level + 1)

        inorder(root, dic, 0)

        for key, val in dic.items():
            res.append(val)

        return res

test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.rightSideView2(head_node)

#     4
#   2   6
#  1 3 5 7