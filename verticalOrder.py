# https://mnmunknown.gitbooks.io/algorithm-notes/content/529_tree.html
# [offset, treenode], if go to head.left then offset -1; head.right then offset + 1, root's offset is 0. Vertical means nodes group by offset
from sortedArrayToBST import Solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def verticalOrder(self, root):

        dic = {}
        offsetTuple = []
        res = []


        if root == None:
            return offsetTuple

        queue = []
        queue.append([0, root])

        # BFS, levelOrderTraversal
        while queue:
            offset, head = queue.pop(0)

            if head.left != None:
                queue.append([offset - 1, head.left])
            if head.right != None:
                queue.append([offset + 1, head.right])
            offsetTuple.append([offset, head.val])

        # list => dic, key = offset
        for t in offsetTuple:
            if t[0] in dic:
                dic[t[0]].append(t[1])
            else:
                dic[t[0]] = [t[1]]

        # Tip: how to sort dic by key
        for key in sorted(dic.iterkeys()):
            res.append(dic[key])
        return res


test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.verticalOrder(head_node)

#    4
#  2   6
# 1 3 5 7