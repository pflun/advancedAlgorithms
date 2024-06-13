# -*- coding: utf-8 -*-
# Definition for a N-ray tree node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

# BFS，serialize成children count + 每一个child value
class Codec:
    def serialize(self, root):
        if root is None:
            return []

        queue = [root]
        res = [root.val]
        while queue:
            node = queue.pop(0)
            if not node:
                continue
            for child in node.children:
                queue.append(child)
            # 注意：如果是empty children [] 这里会count 0，那么deserialize时就不append children
            res.append(len(node.children))  # add count of children
            res.extend([child.val for child in node.children])  # add children values

        return res

    def deserialize(self, data):
        if not data:
            return None

        root = Node(data[0], [])  # get root from first index
        data = data[1:]  # remove root from data
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node is None:
                continue
            for _ in range(data.pop(0)):  # check children count
                child = Node(data.pop(0), [])  # get child value
                node.children.append(child)
                queue.append(child)

        return root

n2 = Node(2, [])
n4 = Node(4, [])
n3 = Node(3, [n4])
n1 = Node(1, [n2, n3])
test = Codec()
print test.serialize(n1)
print test.deserialize(test.serialize(n1)).children[1].children[0].val