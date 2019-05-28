# -*- coding: utf-8 -*-
# http://bookshadow.com/weblog/2017/08/21/leetcode-equal-tree-partition/
# 给定二叉树，求是否存在一条边，将该边切断后得到的两个新二叉树的和相等。
# 遍历各节点，判断该节点的子树和 * 2 == 根节点的节点和

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def checkEqualTree(self, root):

        def getSum(root, res):
            stack = [root]

            while stack:
                curr = stack.pop()
                res += curr.val
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)

            return res

        queue = [root]

        while queue:
            curr = queue.pop(0)
            pSum = getSum(curr, 0)

            if curr.left:
                lSum = getSum(curr.left, 0)
                if lSum * 2 == pSum:
                    return True
                queue.append(curr.left)
            if curr.right:
                rSum = getSum(curr.right, 0)
                if rSum * 2 == pSum:
                    return True
                queue.append(curr.right)

        return False

head_node = TreeNode(5)
n1 = TreeNode(10)
n2 = TreeNode(10)
n3 = TreeNode(2)
n4 = TreeNode(3)

head_node.left = n1
head_node.right = n2
n2.left = n3
n2.right = n4

test1 = Solution()
print test1.checkEqualTree(head_node)