# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        binary = ""
        while head:
            binary += str(head.val)
            head = head.next
        return int(binary, 2)
