# -*- coding: utf-8 -*-
# Segment tree: https://www.youtube.com/watch?v=rYBtViWXYeI
# Id allocator. Capacity 0-N.
# int Allocate() : returns available ID within 0-N range.
# int Release(int ID) : releases given ID and that ID becomes available for allocation.
# Write O(1) solution. After doing that the result was space (N).
class SegmentTreeNode(object):
    def __init__(self, start, end, available, left, right):
        self.start = start
        self.end = end
        self.available = available
        self.left = left
        self.right = right


class SegmentTree(object):
    def build(self, start, end, IDs):
        # 叶子节点
        if start == end:
            return SegmentTreeNode(start, end, [IDs[start]], None, None)
        mid = (start + end) / 2
        left = self.build(start, mid, IDs)
        right = self.build(mid + 1, end, IDs)
        return SegmentTreeNode(start, end, left.available + right.available, left, right)

    # releases given ID and that ID becomes available for allocation.
    def release(self, root, id):
        if root.start == root.end == id:
            root.available = [id]
        mid = (start + end) / 2
        if id <= mid:
            self.update(root.left, id)
        else:
            self.update(root.right, id)
        # 更新每个节点的available
        root.available = root.left.available + root.right.available

    # returns avilable ID within 0-N range.
    def allocate(self, root, i, j):
        # 当前节点的start end刚好覆盖（是要找的）
        if root.start == i and root.end == j:
            return root.available
        mid = (start + end) / 2
        # 要找的区间在左半部分
        if j <= mid:
            return self.allocate(root.left, i, j)
        # 完全被右半部分覆盖
        elif i > mid:
            return self.allocate(root.right, i, j)
        # 一部分被左边覆盖，另一部分被右边覆盖
        else:
            return self.allocate(root.left, i, mid) + self.allocate(root.right, mid + 1, j)