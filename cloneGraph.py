# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def cloneGraph2(self, node):
        dic = {node:UndirectedGraphNode(node.label)}
        queue = [node]

        # Clone nodes
        while queue:
            curr = queue.pop(0)
            for n in curr.neighbors:
                # not visited
                if n not in dic:
                    clone = UndirectedGraphNode(n.label)
                    dic[n] = clone
                    queue.append(n)

        # Clone edges
        for node, cloneNode in dic.items():
            for e in node.neighbors:
                cloneNode.neighbors.append(dic[e])
        return dic


    def cloneGraph(self, node):
        root = node
        if node is None:
            return node

        # use bfs algorithm to traverse the graph and get all nodes.
        nodes = self.getNodes(node)

        # copy nodes, store the old->new mapping information in a hash map
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)

        # copy neighbors(edges)
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    def getNodes(self, node):
        import collections
        q = collections.deque([node])
        result = set([node])
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    q.append(neighbor)
        return result


head = UndirectedGraphNode(1)
p2 = UndirectedGraphNode(2)
p3 = UndirectedGraphNode(3)
p4 = UndirectedGraphNode(4)
head.neighbors = [p2, p3]
p2.neighbors = [head, p4]
p3.neighbors = [head, p4]
p4.neighbors = [p2, p3]
test = Solution()
print test.cloneGraph2(head)[p2].neighbors[0].label, test.cloneGraph2(head)[p2].neighbors[1].label