class Solution(object):
    def printTree(self, root):
        def get_height(node):
            return 0 if not node else 1 + max(get_height(node.left), get_height(node.right))

        def update_output(node, row, left, right):
            if not node:
                return
            mid = (left + right) / 2
            self.output[row][mid] = str(node.val)
            update_output(node.left, row + 1, left, mid - 1)
            update_output(node.right, row + 1, mid + 1, right)

        height = get_height(root)
        width = 0
        for _ in range(height):
            width = width * 2 + 1

        self.output = [["" for _ in range(width)] for _ in range(height)]
        update_output(root, 0, 0, width - 1)
        return self.output