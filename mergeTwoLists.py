class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        tmp = ListNode(0)
        dummy = tmp
        # dummy = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next

        tmp.next = l1 or l2
        # print tmp.val , tmp.next , l1 , l2
        return dummy.next

    def mergeTwoLists2(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy

        # Tip to merge two linked list
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # If any leftover
        if l1 != None:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next

    # test link list
    def testfunc(self, l1):
        l1 = l1.next

        return l1



head = ListNode(1)
p1 = ListNode(3)
p2 = ListNode(5)
p3 = ListNode(7)
head.next = p1
p1.next = p2
p2.next = p3

head2 = ListNode(2)
q1 = ListNode(4)
q2 = ListNode(6)
q3 = ListNode(8)
head2.next = q1
q1.next = q2
q2.next = q3

test = Solution()
test = test.mergeTwoLists(head, head2)
# test2 = Solution()
# test2 = test2.testfunc(head)

while test:
    print test.val
    test = test.next

# while test2:
#     print test2.val
#     test2 = test2.next