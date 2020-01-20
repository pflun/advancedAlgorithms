from sortedArrayToBST import Solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def getAllElements(self, root1, root2):
        self.res = []
        self.stack1 = []
        self.stack2 = []
        while root1:
            self.stack1.append(root1)
            root1 = root1.left

        while root2:
            self.stack2.append(root2)
            root2 = root2.left

        while self.stack1 and self.stack2:
            if self.stack1[-1].val < self.stack2[-1].val:
                self.res.append(self.next1())
            elif self.stack1[-1].val > self.stack2[-1].val:
                self.res.append(self.next2())
            else:
                self.res.append(self.next1())
                self.res.append(self.next2())
        if len(self.stack1) > 0:
            while self.stack1:
                self.res.append(self.next1())
        elif len(self.stack2) > 0:
            while self.stack2:
                self.res.append(self.next2())
        return self.res

    def next1(self):
        node = self.stack1.pop()
        x = node.right
        while x:
            self.stack1.append(x)
            x = x.left
        return node.val

    def next2(self):
        node = self.stack2.pop()
        x = node.right
        while x:
            self.stack2.append(x)
            x = x.left
        return node.val

test = Solution()
head_node1 = test.sortedArrayToBST([1, 3, 5, 7])
head_node2 = test.sortedArrayToBST([2, 3, 4, 6, 7, 8])
test1 = Solution1()
print test1.getAllElements(head_node1, head_node2)