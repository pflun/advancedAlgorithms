# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
        self.count = 1

    def __str__(self):
        return 'value: {0}, count: {1}'.format(self.value, self.count)

def insert(root, value):
    if not root:
        return TreeNode(value)
    elif root.value == value:
        root.count += 1
    elif value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root

def create(seq):
    root = None
    for word in seq:
        root = insert(root, word)

    return root

def search(root, word, depth=1):
    if not root:
        return 0, 0
    elif root.value == word:
        return depth, root.count
    elif word < root.value:
        return search(root.left, word, depth + 1)
    else:
        return search(root.right, word, depth + 1)

def print_tree(root):
    if root:
        print_tree(root.left)
        print root
        print_tree(root.right)

class Solution(object):
    def isSymmetric2(self, root):
        if not root:
            return True

        def helper(node1, node2):
            if not node1 or not node2:
                if not node1 and not node2:
                    return True
                else:
                    return False
            if node1.val != node2.val:
                return False
            left = helper(node1.left, node2.right)
            right = helper(node1.right, node2.left)
            if left and right:
                return True
            else:
                return False

        return helper(root.left, root.right)


    def isSymmetric(self, root):
        child_left = root.left
        child_right = root.right
        stack = [(child_left, child_right)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                stack.append((node1.right, node2.left))
                stack.append((node1.left, node2.right))
        return True


tree = create([1,2,2,3,4,4,3])
print_tree(tree)
print tree

test = Solution()
print test.isSymmetric(tree)