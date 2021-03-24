class Solution(object):
    def findLeaves(self, root):
        output = collections.defaultdict(list)

        def dfs(node, layer):
            if not node:
                return layer
            left = dfs(node.left, layer)
            right = dfs(node.right, layer)
            layer = max(left, right)
            output[layer].append(node.val)
            return layer + 1

        dfs(root, 0)
        return output.values()