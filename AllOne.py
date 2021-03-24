# https://leetcode.com/problems/all-oone-data-structure/discuss/1059478/python3-clean-code-doubly-linked-list-%2B-hash-table
# The basic idea is to keep a hash table recoding the mapping from keys to the values, then another hash table recording the mapping from values to nodes in doubly-linked list.
# Each node will record the keys stored, and the corresponding value.
# When inc(), locate the node, remove the key from the keys stored in the node, increment value by 1, and add the key into the next node.
# When dec(), locate the node, remove the key from the keys stored in the node, decrement value by 1, and add the key into the previous node.
# The doubly-linked list allowed us to insert and delete by O(1). For min and max operation, just look at the head and the tail of the linked list.
class Node():
    def __init__(self, val):
        self.val = val
        self.keys = set()
        self.next = None
        self.prev = None


class AllOne:

    def __init__(self):
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.keys.add('#')
        self.tail.keys.add('#')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key2val = defaultdict(int)
        self.val2node = defaultdict(Node)

    def insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def insert_before(self, node, new_node):
        new_node.prev = node.prev
        new_node.next = node
        node.prev.next = new_node
        node.prev = new_node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def inc(self, key):
        if key in self.key2val:
            old_val = self.key2val[key]
            node = self.val2node[old_val]
            node.keys.remove(key)
            new_val = old_val + 1
        else:
            node = self.head
            new_val = 1

        if new_val != node.next.val:
            new_node = Node(new_val)
            self.insert_after(node, new_node)
        else:
            new_node = node.next
        new_node.keys.add(key)

        if not node.keys:
            del self.val2node[node.val]
            self.remove(node)
        self.key2val[key] = new_val
        self.val2node[new_val] = new_node

    def dec(self, key):
        if key not in self.key2val:
            return

        old_val = self.key2val[key]
        node = self.val2node[old_val]
        node.keys.remove(key)
        del self.key2val[key]
        new_val = old_val - 1
        if new_val != 0:
            if new_val != node.prev.val:
                new_node = Node(new_val)
                self.insert_before(node, new_node)
            else:
                new_node = node.prev
            new_node.keys.add(key)
            self.key2val[key] = new_val
            self.val2node[new_val] = new_node

        if not node.keys:
            del self.val2node[node.val]
            self.remove(node)

    def getMaxKey(self):
        if self.tail.prev != self.head:
            return next(iter(self.tail.prev.keys))
        else:
            return ''

    def getMinKey(self):
        if self.head.next != self.tail:
            return next(iter(self.head.next.keys))
        else:
            return ''
