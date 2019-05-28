#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    # recursively
    def invertTree(self, root):
        if root:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)

            root.left, root.right = right, left

            return root

    # BFS
    # def invertTree2(self, root):
    #     queue = collections.deque([(root)])
    #     while queue:
    #         node = queue.popleft()
    #         if node:
    #             node.left, node.right = node.right, node.left
    #             queue.append(node.left)
    #             queue.append(node.right)
    #     return root

    # DFS
    def invertTree1(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])
        return root

    def preTraverse(self, root):
        if root == None:
            return
        print root.val
        self.preTraverse(root.left)
        self.preTraverse(root.right)

    def midTraverse(self, root):
        if root == None:
            return
        self.midTraverse(root.left)
        print root.val
        self.midTraverse(root.right)

    def postTraverse(self, root):
        if root == None:
            return
        self.postTraverse(root.left)
        self.postTraverse(root.right)
        print root.val

head = TreeNode(1)
p1 = TreeNode(2)
p2 = TreeNode(3)
p3 = TreeNode(4)
head.left = p1
head.right = p2
p1.left = p3

test = Solution()
test.invertTree(head)
test.postTraverse(head)

# while head:
#     print head.val
#     head = head.right
