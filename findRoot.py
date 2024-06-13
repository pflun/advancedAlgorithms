class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

# No need to construct tree, the Leetcode examples are confusing, looks like input just list of nodes, tree[0] is not root
# Root is not in any nodes's children, all non-root will appear in other nodes's children
# Just loop through children, then loop through all nodes(tree), root won't appear in second loop
class Solution(object):
    def findRoot(self, tree):
        children = set()
        for t in tree:
            for c in t.children:
                children.add(c.val)
        for t in tree:
            if t.val not in children:
                return t
        return None

test = Solution()
print test.findRoot([])