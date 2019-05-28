class ListNode:
    def __init__(self, x):
        self.val = x;
        self.next = None;


def nonrecurse(head):
    if head is None or head.next is None:
        return head;
    pre = None;
    cur = head;
    h = head;
    while cur:
        h = cur;
        tmp = cur.next;
        cur.next = pre;
        pre = cur;
        cur = tmp;
    return h;

def reverseList(head):
    rev = None
    while head:
        # head.next = rev
        # rev = head
        # head = head.next
        head.next, rev, head = rev, head, head.next
    return rev

def reverseLinkedList(head):
    dummy = ListNode(0)
    # Use 2 or more nodes as example
    # Test case: 1, 2 then return 2 (meanwhile if print (p.next).val you will get 1)
    while head:
        tmp = head.next # store tmp, for step 4 to move forward
        head.next = dummy.next # reverse: 1.next -> null, 2nd while 2.next -> 1
        dummy.next = head # dummy.next -> 1, 2nd while dummy.next -> 2
        head = tmp # head forward
    return dummy.next #loop twice if 2 nodes, loop 3 times if 3 nodes etc

def reverseLinkedList2(head):
    if not head:
        return None
    stack = []
    dummy = ListNode(0)
    dummy.next = head
    tail = dummy

    while head:
        stack.append(head)
        head = head.next

    while stack:
        tail.next = stack.pop()
        tail = tail.next

    # On last node, you have to point to None (bc it was point to second node)
    tail.next = None

    return dummy.next

head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(4)
head.next = p1
p1.next = p2
p2.next = p3
p = reverseLinkedList2(head)

while p:
    print p.val
    p = p.next