# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def countPairs(self, root, distance):
        self.res = 0

        def postorder(root):
            if root is None:
                return []
            
            # 叶子节点返回距离列表，初始距离父节点为 1
            if root.left is None and root.right is None:
                return [1]

            left = []
            if root.left:
                left = postorder(root.left)

            right = []
            if root.right:
                right = postorder(root.right)

            # 左右子树都存在，组合计算叶子节点间的距离
            if left and right:
                for l in left:
                    for r in right:
                        if l + r <= distance:
                            self.res += 1

            # 把当前左右子树的距离 + 1 后向上返回给父节点
            # 优化：只返回距离严格小于 distance 的叶子节点，因为如果距离已经 >= distance，
            # 加上另一边至少为 1 的距离后，必然 > distance，无法再组成好叶子对。
            current_distances = []
            for l in left:
                if l + 1 < distance:
                    current_distances.append(l + 1)
            for r in right:
                if r + 1 < distance:
                    current_distances.append(r + 1)

            return current_distances

        postorder(root)

        return self.res