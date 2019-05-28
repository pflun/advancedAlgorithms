# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        self.dic = {}
        self.res = []
        self.faq = 0

        def getSum(root, res):
            stack = [root]
            while stack:
                curr = stack.pop()
                res += curr.val
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
            return res

        queue = [root]
        while queue:
            tmp = queue.pop(0)
            tmpsum = getSum(tmp, 0)
            self.dic[tmpsum] = self.dic.get(tmpsum, 0) + 1

            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)

        for key, val in self.dic.items():
            if val > self.faq:
                self.faq = val
                self.res = [key]
            elif val == self.faq:
                self.res.append(key)

        return self.res

head_node = TreeNode(5)
n1 = TreeNode(2)
n2 = TreeNode(-5)
head_node.left = n1
head_node.right = n2

test = Solution()
print test.findFrequentTreeSum(head_node)