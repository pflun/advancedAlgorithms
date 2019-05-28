# -*- coding: utf-8 -*-
from sortedArrayToBST import Solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def validCompleteTree(self, root):
        dic = {}
        level = 0
        self.inorder(root, dic, level)

        # perfect tree
        # tip: last key -- dic.keys()[-1], last value -- dic.values()[-1]
        # if last row is full
        if len(dic.values()[-1]) == 2 ** dic.keys()[-1]:
            # should be all #
            for i in dic.values()[-1]:
                if i != '#':
                    return False
            for j in dic.values()[:-1]:
                for k in j:
                    if k == '#':
                        return False
        # not perfect tree
        else:
            # should be all # after some point
            flag = False
            for i in dic.values()[-2]:
                if flag is False and i == '#':
                    flag = True
                elif flag is True and i != '#':
                    return False
            for j in dic.values()[:-2]:
                for k in j:
                    if k == '#':
                        return False

        return True

    def inorder(self, root, dic, level):
        if root == None:
            if level in dic:
                dic[level].append('#')
            else:
                dic[level] = ['#']
            return None

        self.inorder(root.left, dic, level + 1)
        if level in dic:
            dic[level].append(root.val)
        else:
            dic[level] = [root.val]
        self.inorder(root.right, dic, level + 1)


test = Solution()
head_node = test.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.validCompleteTree(head_node)

#     4
#   2   6
#  1 3 5 7
# 0