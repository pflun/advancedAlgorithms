class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements(object):

    def __init__(self, root):
        self.root = root
        self.recover(root, 0)

    def recover(self, node, value):
        node.val = value
        if node.left:
            self.recover(node.left, 2 * value + 1)
        if node.right:
            self.recover(node.right, 2 * value + 2)

    def find(self, target):
        path = []
        while target != 0:
            path.append(target)
            if target % 2 == 0:
                target = (target - 2) / 2
            else:
                target = (target - 1) / 2
        path.append(0)
        return self.search(self.root, path[::-1], 0)

    def search(self, root, path, i):
        if root.val != path[i]:
            return False
        if i == len(path) - 1:
            return True
        if path[i + 1] % 2 == 1 and root.left:
            return self.search(root.left, path, i + 1)
        elif path[i + 1] % 2 == 0 and root.right:
            return self.search(root.right, path, i + 1)
        else:
            return False

head_node = TreeNode(-1)
n1 = TreeNode(-1)
n2 = TreeNode(-1)
n3 = TreeNode(-1)
n4 = TreeNode(-1)
n5 = TreeNode(-1)
n6 = TreeNode(-1)
n7 = TreeNode(-1)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
n3.left = n5
n5.left = n6
n5.right = n7

test1 = FindElements(head_node)
print test1.find(16)

#     0
#   1   2
#  3 4
# 7
#15 16