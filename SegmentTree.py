# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=rYBtViWXYeI
class SegmentTreeNode(object):
    def __init__(self, start, end, sum, left, right):
        self.start = start
        self.end = end
        self.sum = sum # can be max / min
        self.left = left
        self.right = right


class SegmentTree(object):
    def build(self, start, end, vals):
        # 叶子节点
        if start == end:
            return SegmentTreeNode(start, end, vals[start], None, None)
        mid = (start + end) / 2
        left = self.build(start, mid, vals)
        right = self.build(mid + 1, end, vals)
        return SegmentTreeNode(start, end, left.sum + right.sum, left, right)

    def update(self, root, index, val):
        if root.start == root.end == index:
            root.sum = val
        mid = (start + end) / 2
        if index <= mid:
            self.update(root.left, index, val)
        else:
            self.update(root.right, index, val)
        # 更新每个节点的sum
        root.sum = root.left + root.right.sum

    def querySum(self, root, i, j):
        # 当前节点的start end刚好覆盖（是要找的）
        if root.start == i and root.end == j:
            return root.sum
        mid = (start + end) / 2
        # 要找的区间在左半部分
        if j <= mid:
            return self.querySum(root.left, i, j)
        # 完全被右半部分覆盖
        elif i > mid:
            return self.querySum(root.right, i, j)
        # 一部分被左边覆盖，另一部分被右边覆盖
        else:
            return self.querySum(root.left, i, mid) + self.querySum(root.right, mid + 1, j)