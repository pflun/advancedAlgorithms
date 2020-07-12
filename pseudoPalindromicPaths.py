# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pseudoPalindromicPaths (self, root):
        if not root:
            return 0
        self.res = 0

        def helper(node, paths):
            if not node.left and not node.right:
                arr = paths.split(';')
                arr += str(node.val)
                dic = {}
                for a in arr[1:]:
                    dic[a] = dic.get(a, 0) + 1
                odd = 0
                for v in dic.values():
                    if v % 2 == 0:
                        continue
                    else:
                        odd += 1
                        if odd > 1:
                            break
                if odd == 0 or odd == 1:
                    self.res += 1

            if node.left:
                helper(node.left, paths + ';' + str(node.val))
            if node.right:
                helper(node.right, paths + ';' + str(node.val))

        helper(root, '')
        return self.res

test = Solution()
head = TreeNode(2)
n1 = TreeNode(3)
n2 = TreeNode(3)
n3 = TreeNode(1)
n4 = TreeNode(1)
n5 = TreeNode(1)
head.left = n1
head.right = n4
n1.left = n2
n1.right = n3
n4.right = n5
print test.pseudoPalindromicPaths(head)