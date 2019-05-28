# -*- coding: utf-8 -*-
# Linked List 如果静态不变，__init__里计算长度，然后每次随机一个就行
# 如果是动态：
# 先选取数据流中的前k个元素，保存在集合A中；
# 从第j（k + 1 <= j <= n）个元素开始，每次先以概率p = k/j选择是否让第j个元素留下。若j被选中，则从A中随机选择一个元素并用该元素j替换它；否则直接淘汰该元素；
# 重复步骤2直到结束，最后集合A中剩下的就是保证随机抽取的k个元素。
# 纯纯的reservoir sampling

import random
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        result, node, index = self.head, self.head.next, 1
        while node:
            if random.randint(0, index) is 0:
                result = node
            node = node.next
            index += 1
        return result.val



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()