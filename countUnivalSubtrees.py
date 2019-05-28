# -*- coding: utf-8 -*-
# 分别看左右子树返回值是否与根相等，分情况讨论
# https://mnmunknown.gitbooks.io/algorithm-notes/content/61_tree.html
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        self.res = 0

        def postorder(root):
            if root is None:
                return None
            # 叶子节点也算一个子树
            if root.left is None and root.right is None:
                self.res += 1
                return root.val

            if root.left:
                left = postorder(root.left)

            if root.right:
                right = postorder(root.right)

            # 左右子树都存在
            if root.left and root.right:
                # 左右儿子和根值相等
                if left == right:
                    if left is root.val:
                        self.res += 1
                    else:
                        return False
                else:
                    # 左儿子和根相等
                    if left == root.val:
                        self.res += 1
                    # 或者右儿子和根相等
                    elif right == root.val:
                        self.res += 1

            # 只存在左子树
            elif root.left and not root.right:
                # 左儿子和根相等
                if left == root.val:
                    self.res += 1
                else:
                    return False

            elif root.right and not root.left:
                if right == root.val:
                    self.res += 1
                else:
                    return False

            return root.val

        postorder(root)

        return self.res


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

test1 = Solution()
print test1.countUnivalSubtrees(head_node)

#     0
#   1   0
#  5 4
# 5
#5 5