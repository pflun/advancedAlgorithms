# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=q1zk8vZIDw0
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):

        # return pair (子树的depth, 当前最优解节点)
        def search(depth, node):
            if not node.left and not node.right:
                return [depth, node]

            left = []
            right = []
            if node.left:
                left = search(depth + 1, node.left)
            if node.right:
                right = search(depth + 1, node.right)

            if len(left) != 0 and len(right) != 0:
                if left[0] == right[0]:
                    return [left[0], node]
                elif left[0] > right[0]:
                    return left
                else:
                    return right
            elif len(left) != 0:
                return left
            elif len(right) != 0:
                return right

        return search(0, root)[1]