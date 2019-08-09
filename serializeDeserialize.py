from sortedArrayToBST import Solution
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        # [0, 1, 3, 5, '#', 6, '#', '#', '#', 4, '#', '#', 2, '#', '#']
        res = []
        self.preorder(root, res)

        return res
    def preorder(self, root, res):
        if root == None:
            res.append('#')
            return

        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

    def deserialize(self, data):
        # https://www.programiz.com/python-programming/methods/built-in/iter
        vals = iter(data)

        root = self.helper(vals)
        return root

    def helper(self, vals):
        # first use next() is the first element in data
        val = next(vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = self.helper(vals)
        node.right = self.helper(vals)
        return node

    def deserialize2(self, data):
        self.data = data
        def helper():
            if self.data[0] == '#':
                self.data.pop(0)
                return None
            node = TreeNode(self.data[0])
            self.data.pop(0)
            node.left = helper()
            node.right = helper()
            return node

        return helper()


head_node = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
n3.left = n5
n5.right = n6

codec = Codec()
print codec.serialize(head_node)
print codec.deserialize2(codec.serialize(head_node)).left.right.right

#     0
#   1   2
#  3 4
# 5
#  6