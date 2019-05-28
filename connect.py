# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # Accept
    def connect(self, root):
        if not root:
            return
        while root.left:
            cur = root.left
            prev = None
            while root:
                # prev -> left
                if prev:
                    prev.next = root.left
                # left -> right
                root.left.next = root.right
                # move prev to right
                prev = root.right
                # move root to next root prepare for next loop
                root = root.next
            # start next row
            root = cur

    def connect2(self, root):

        if root == None:
            return root

        queue = [root]

        while queue:
            size = len(queue)
            prev = None
            for i in range(size):
                head = queue.pop(0)
                if prev:
                    prev.next = head
                if head.left != None:
                    queue.append(head.left)
                if head.right != None:
                    queue.append(head.right)
                prev = head

        return root

head_node = TreeLinkNode(0)
n1 = TreeLinkNode(1)
n2 = TreeLinkNode(2)
n3 = TreeLinkNode(3)
n4 = TreeLinkNode(4)
n5 = TreeLinkNode(5)
n6 = TreeLinkNode(6)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
n3.left = n5
n5.right = n6

test = Solution()
print test.connect2(head_node).left.left.next.val

#     0
#   1   2
#  3 4
# 5
#  6