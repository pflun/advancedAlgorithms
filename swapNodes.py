# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapNodes(self, head, k):
        dummy = head
        front = head
        back = head
        length = 0
        while head:
            head = head.next
            length += 1
        if length == 1:
            return dummy
        for _ in range(k - 1):
            front = front.next
        for _ in range(length - k):
            back = back.next
        if front.val != back.val:
            front.val, back.val = back.val, front.val
        return dummy