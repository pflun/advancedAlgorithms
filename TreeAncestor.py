# TLE, use TreeMap
class TreeAncestor(object):

    def __init__(self, n, parent):
        self.dic = {}
        for i in range(n):
            self.dic[i] = parent[i]

    def getKthAncestor(self, node, k):
        while k > 0 and self.dic[node] != -1:
            node = self.dic[node]
            k -= 1
        if k == 0:
            return node
        else:
            return -1

test = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
print test.getKthAncestor(3, 1)
print test.getKthAncestor(5, 2)
print test.getKthAncestor(6, 3)