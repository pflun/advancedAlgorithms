class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# work on no duplicates
class Solution(object):
    def insert(self, head, insertVal):
        back = head
        front = head
        front = front.next

        while True:
            # normal case
            if front.val > insertVal and back.val < insertVal:
                newNode = ListNode(insertVal)
                back.next = newNode
                newNode.next = front
                break
            # insert 0 to 1 -> 5, or 6 to 1 -> 5
            elif front.val < back.val:
                newNode = ListNode(insertVal)
                back.next = newNode
                newNode.next = front
                break
            back = back.next
            front = front.next

        return head

head = ListNode(1)
p1 = ListNode(3)
p2 = ListNode(4)
p3 = ListNode(6)
p4 = ListNode(7)
head.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = head

test = Solution()
traverse = test.insert(head, 0)
cnt = 0
while cnt < 10:
    print traverse.val
    traverse = traverse.next
    cnt += 1