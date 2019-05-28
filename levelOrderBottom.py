from sortedArrayToBST import Solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def levelOrderBottom(self, root):
        stack = []
        res = []

        if root == None:
            return res

        from Queue import Queue
        queue = Queue()
        queue.put(root)

        while not queue.empty():
            level = []
            size = queue.qsize()
            for i in range(size):
                head = queue.get()
                level.append(head.val)
                if head.left != None:
                    queue.put(head.left)
                if head.right != None:
                    queue.put(head.right)
            stack.append(level)

        while stack:
            res.append(stack.pop())

        return res

test = Solution()
head_node = test.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
test1 = Solution1()
print test1.levelOrderBottom(head_node)

#    4
#  2   6
# 1 3 5 7