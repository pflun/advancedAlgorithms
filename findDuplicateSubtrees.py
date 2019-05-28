# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        dic = {}
        ans = []

        # serialize
        def serialize(root):
            res = []
            def postorder(root, res):
                if root is None:
                    res.append('#')
                    return None
                postorder(root.left, res)
                postorder(root.right, res)
                res.append(str(root.val))

            postorder(root, res)

            return ''.join(res)

        def inorder(root, dic):
            if not root:
                return None

            if root.left:
                inorder(root.left, dic)

            # ##1#2#3#4#5 => [dup_root1, dup_root2, dup_root3]
            tmp = serialize(root)
            if tmp not in dic:
                dic[tmp] = [root]
            else:
                dic[tmp].append(root)

            if root.right:
                inorder(root.right, dic)

            return dic

        inorder(root, dic)

        for key, val in dic.items():
            # if duplicates
            if len(val) > 1:
                ans.append(val)

        return ans



head_node = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n55 = TreeNode(5)
n66 = TreeNode(6)
n77 = TreeNode(7)
head_node.left = n1
head_node.right = n2
n1.left = n3
n1.right = n4
n3.left = n6
n6.left = n5
n6.right = n7
n2.right = n66
n66.left = n55
n66.right = n77

test1 = Solution()
print test1.findDuplicateSubtrees(head_node)

#     0
#   1   2
#  3 4   6
# 6     5 7
#5 7