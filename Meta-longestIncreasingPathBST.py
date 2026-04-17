from sortedArrayToBST import Solution
# Similar to diameterOfBinaryTree except returning max(left, right) + 1, your helper function tells the parent node
# the length of the longest path downwards, regardless of whether it went left or right.
class Solution1(object):
    def longestIncreasingPathBST(self, root):
        if not root:
            return 0
        self.res = 0

        def helper(node):
            if not node:
                return 0, 0
            left_child_left_spine, _ = helper(node.left)
            _, right_child_right_spine = helper(node.right)
            left_spine = 1 + left_child_left_spine if node.left else 0
            right_spine = 1 + right_child_right_spine if node.right else 0

            self.res = max(self.res, left_spine + right_spine + 1)

            return left_spine, right_spine

        helper(root)
        return self.res

    def longestIncreasingPathBinaryTree(self, root):
        if not root:
            return 0
        self.max_len = 0
        def dfs(node):
            if not node:
                return 0, 0
            left_inc, left_dec = dfs(node.left)
            right_inc, right_dec = dfs(node.right)
            # Every node is at least a path of length 1 (just itself)
            curr_inc = 1
            curr_dec = 1

            # Check left child
            if node.left:
                if node.left.val > node.val:
                    # The longest path extending strictly downwards where values get larger.
                    curr_inc = max(curr_inc, left_inc + 1)
                elif node.left.val < node.val:
                    curr_dec = max(curr_dec, left_dec + 1)

            # Check right child
            if node.right:
                if node.right.val > node.val:
                    curr_inc = max(curr_inc, right_inc + 1)
                elif node.right.val < node.val:
                    curr_dec = max(curr_dec, right_dec + 1)

            # Stitch the best downward increasing and downward decreasing paths together.
            # (If they only exist on one side, one of these values will just be 1,
            # correctly representing a path that doesn't cross the node).
            self.max_len = max(self.max_len, curr_inc + curr_dec - 1)

            # Return strictly downward paths to the parent
            return curr_inc, curr_dec

        dfs(root)
        return self.max_len

test = Solution()
head_node = test.sortedArrayToBST([0, 1, 2, 4, 5, 3, 6, 7])
test1 = Solution1()
print test1.longestIncreasingPathBST(head_node)

#     5
#   2   6
#  1 4 3 7
# 0