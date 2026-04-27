# 1265 - Print Immutable Linked List in Reverse
class ImmutableListNode(object):
    def printValue(self):
        pass

    def getNext(self):
        pass

class Solution(object):
    def printLinkedListInReverse(self, head):
        if not head:
            return
        n = self.get_count(head)
        for i in range(n, 0, -1):
            self.print_nth(head, i)

    def get_count(self, head):
        count = 0
        current = head
        while current:
            count += 1
            current = current.getNext()
        return count

    def print_nth(self, head, n):
        curr = head
        for i in range(n - 1):
            if not curr:
                return
            curr = curr.getNext()

        curr.printValue()