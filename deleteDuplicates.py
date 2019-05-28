#Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return dummy.next





head = ListNode(0)
p1 = ListNode(2)
p2 = ListNode(2)
p3 = ListNode(2)
p4 = ListNode(7)
head.next = p1
p1.next = p2
p2.next = p3
p3.next = p4

test = Solution()
test.deleteDuplicates(head)

while head:
    print head.val
    head = head.next