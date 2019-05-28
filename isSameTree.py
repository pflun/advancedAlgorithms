def isSameTree(self, p, q):
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    return p is q

def isSameTree1(self, p, q):
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    else:
        return p == q


# DFS with stack
def isSameTree2(self, p, q):
    stack = [(p, q)]
    while stack:
        node1, node2 = stack.pop()
        if not node1 and not node2:
            continue
        elif None in [node1, node2]:
            return False
        else:
            if node1.val != node2.val:
                return False
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
    return True


# BFS with queue
def isSameTree3(self, p, q):
    queue = [(p, q)]
    while queue:
        node1, node2 = queue.pop(0)
        if not node1 and not node2:
            continue
        elif None in [node1, node2]:
            return False
        else:
            if node1.val != node2.val:
                return False
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
    return True