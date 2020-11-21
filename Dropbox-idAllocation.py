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
            self.release(root.left, id)
        else:
            self.release(root.right, id)
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

# Solution 2: Segment tree + bit arrya
# 最底下一层bit array表示那个index所代表的id有没有被占用。然后每往上一层array也是用bit存，
# 是指左边或右边的subarray里有没有available id。如果root是0，就说明整个array里都没有available ID；如果root是1，
# 那就可以继续顺着他是1的child往下找.....这样allocate的时间就是.....O(logN)。找到以后在bottom up都update一遍，allocate的时间还是O(logN)吧
# 最下层0/1，上面每一层0/1代表没有available/有available
class TreeNode(object):
    def __init__(self, start, end, isAvailable, left, right):
        self.start = start
        self.end = end
        self.isAvailable = isAvailable
        self.left = left
        self.right = right

class Solution2(object):
    def __init__(self, root):
        self.root = root

    def build(self, start, end):
        # 叶子节点
        if start == end:
            return TreeNode(start, end, 1, None, None)
        mid = (start + end) / 2
        left = self.build(start, mid)
        right = self.build(mid + 1, end)
        return TreeNode(start, end, 1, left, right)

    def allocate(self, root, i):
        if root.isAvailable == 0:
            return False
        if root.start == root.end == i:
            root.isAvailable = 0
            return True
        mid = (start + end) / 2
        if i <= mid:
            res = self.allocate(root.left, i)
        else:
            res = self.allocate(root.right, i)
        if root.left.isAvailable == 0 and root.right.isAvailable == 0:
            root.isAvailable = 0
        return res

    def release(self, root, id):
        if root.start == root.end == id:
            root.isAvailable = 1
        mid = (start + end) / 2
        if id <= mid:
            self.release(root.left, id)
        else:
            self.release(root.right, id)
        if root.left.isAvailable == 1 or root.right.isAvailable == 1:
            root.isAvailable = 1