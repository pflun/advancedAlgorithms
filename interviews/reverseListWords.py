# -*- coding: utf-8 -*-
# 把link list中的每个词语reverse，不用改变单词的相对顺序。
# e.g.  H -> E -> L -> L -> O -> ' ' -> W -> O - > R -> L -> D ->NULL
# reverse 之后： O -> L -> L -> E -> H -> ' ' -> D -> L - > R -> O -> W ->NULL
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseListWords(self, head):
        # start of each word
        start = head
        # end of each word after reverse, will be used later when connect end to the newly reversed head
        end = None
        res = None
        while head and head.next:
            if head.next.val == " ":
                # save next start
                tmp = head.next.next
                # break current word
                head.next = None
                # reverse current word
                newHead, tail = self.reverse(start)
                # connect last letter from last word to new head
                if end:
                    # add " "
                    end.next = ListNode(" ")
                    # connect last reversed tail to the newly reversed start
                    end.next.next = newHead
                end = tail
                # new head is the last letter of the first word
                if res is None:
                    res = newHead
                # reset start
                start = tmp
                head = start
            else:
                head = head.next
        # reverse last word
        if start:
            newHead, tail = self.reverse(start)
            end.next = ListNode(" ")
            end.next.next = newHead
        return res

    def reverse(self, head):
        newHead = ListNode(0)
        tail = head
        while head:
            tmp = head.next
            head.next = newHead.next
            newHead.next = head
            head = tmp
        return newHead.next, tail


head = ListNode("H")
p1 = ListNode("E")
p2 = ListNode("L")
p3 = ListNode("L")
p4 = ListNode("O")
p5 = ListNode(" ")
p6 = ListNode("W")
p7 = ListNode("O")
p8 = ListNode("R")
p9 = ListNode("L")
p10 = ListNode("D")
head.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p7
p7.next = p8
p8.next = p9
p9.next = p10
test = Solution()
p = test.reverseListWords(head)
# print test.reverseListWords2(head)[0].val, test.reverseListWords2(head)[1].val

while p:
    print p.val
    p = p.next