# Each time we scan two characters, the first character is either ? or :, the second character holds the value of the tree node.
# When we see ?, we add the new node to left.
# When we see :, we need to find out the ancestor node that doesn't have a right node, and make the new node as its right child.
#
# Time complexity is O(n).

class Node(object):
    """  Tree Node """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder_tree(node, result):
   """ Access Tree in-order """
   if node is not None:
       inorder_tree(node.left, result)
       result.append(node.data)
       inorder_tree(node.right, result)


def ternary_to_binary_tree(expression):
    """ Convert ternary expression to Binary Tree """
    if not expression:
        return None

    # Assuming the expression is of correct form
    stack = []
    root = Node(expression[0])
    stack.append(root)

    for index in range(1, len(expression), 2):
        operator = expression[index]
        next_char = expression[index + 1]
        node = Node(next_char)
        if operator == "?":
            stack[-1].left = node

        if operator == ':':
            stack.pop()
            while(stack[-1].right != None):
                stack.pop()
            stack[-1].right = node


        stack.append(node)

    return root

def preorder_tree(root):
    """ Preorder + push ? or : into stack """
    stack = [root]
    res = ''

    while stack:
        curr = stack.pop()
        if curr == '?' or curr ==':':
            res += curr
        else:
            res += curr.data
            if curr.right:
                stack.append(curr.right)
                stack.append(':')
            if curr.left:
                stack.append(curr.left)
                stack.append('?')

    return res


# print ternary_to_binary_tree("a?b?c:d:e").right.data
print preorder_tree(ternary_to_binary_tree("a?b?c:d:e"))

# "a?b?c:d:e"
#     a
#    / \
#   b   e
#  / \
# c   d