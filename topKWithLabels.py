# -*- coding: utf-8 -*-
# value: 9,  8,  6, 8, 7.
# label:  A, A, B, A,B
# 输入一些node, node里有value和label, 找出K个value最大的, 但每个label不能超过M个. 比如K=3, M=2, 答案是 9,  8, 7.  8 > 7, 但是A的数量不能超过2.
# A, A, B  A    B
# 先sort by value再从大到小scan，复杂度O(nlogn).
# Solution 2: 对每个label用heap选出M个最大的, 然后再从这些用heap选出K个最大的, 最后就是O(nlogk)
class Node(object):
    def __init__(self, value, label):
        self.value = value
        self.label = label

class Solution(object):
    def topKWithLabels(self, nodes, k, m):
        nodes.sort(key=lambda x: x.value, reverse=True)
        cnt = {}
        res = []
        for n in nodes:
            if len(res) == k:
                return res
            cnt[n.label] = cnt.get(n.label, 0) + 1
            if n.label in cnt and cnt[n.label] > m:
                cnt[n.label] = cnt.get(n.label, 0) - 1
                continue
            else:
                res.append(n)