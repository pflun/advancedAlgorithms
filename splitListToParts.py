# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        res = []
        size = 0
        traverse = root
        while traverse:
            size += 1
            traverse = traverse.next

        # 制作一个queue，[4, 3, 3]，代表每一回合走几步
        d, r = divmod(size, k)
        queue = []
        for _ in range(d):
            queue.append(k)
        for i in range(r):
            queue[i] += 1

        # 从queue里取该回合走的步数，一边走一边加入tmp，然后tmp加入res
        for q in queue:
            tmp = []
            for _ in range(q):
                tmp.append(root)
                root = root.next
            res.append(tmp)

        return res

head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(4)
p4 = ListNode(5)
p5 = ListNode(6)
p6 = ListNode(7)
p7 = ListNode(8)
p8 = ListNode(9)
p9 = ListNode(10)
head.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p7
p7.next = p8
p8.next = p9

test = Solution()
print test.splitListToParts(head, 3)