# 1650 - Lowest Common Ancestor of a Binary Tree III
# Return LCA, each node will have a reference to its parent node.
# Add all P ancestors into set() using parent pointer, move q upwards to root, the first q ancestor in P's set() is LCA
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        setP = set(root.val)
        while p != root:
            setP.add(p.val)
            p = p.parent
        while q:
            if q.val in setP:
                return q
            q = q.parent
        return None