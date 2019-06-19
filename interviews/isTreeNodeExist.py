# -*- coding: utf-8 -*-
# tree node 定义是 class Node { Node left, right }; 不需要value. 然后每个node隐含一个 id. 比如
#         x
#        / \
#       x  x
#        \   \
#         x   x
# 那么第一行的node id = 1, 第二行 node id = 2, 3, 第三行 node id = 5, 7。 说白了，每个node的id就是假设这是个perfect tree的话， 那么这个node的序号。
# 1. 给一个ID，判断这个id 对应的node 是否在tree里面。 要求 lgN.
# 2. 如果这是一个 compelete tree, 注意 complete tree != perfect tree. 那么这个tree 里面有多少个node. 时间复杂度要求不能比 (lgN)^2 差。
#     x
#    / \
# 2x   2x+1
from sortedArrayToBST import Solution
class Solution1(object):
    def isTreeNodeExist(self, root, id):
        path = []
        while id != 1:
            path.append(id)
            id = id / 2
        return self.search(root, path[::-1], 0)

    def search(self, root, path, i):
        # 小bug，id = 9
        if i == len(path) - 1:
            return True
        if path[i] % 2 == 0 and root.left:
            return self.search(root.left, path, i + 1)
        elif path[i] % 2 == 1 and root.right:
            return self.search(root.right, path, i + 1)
        else:
            return False

testBST = Solution()
root = testBST.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7])
test = Solution1()
print test.isTreeNodeExist(root, 9)

# Ignore the number, 4 should be 1, 6 should be 3
#     4
#   2   6
#  1 3 5 7
# 0