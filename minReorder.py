class Solution(object):
    def minReorder(self, n, connections):
        res = 0
        visited = set([0])
        neighbors = {}
        dic = {}
        for c in connections:
            neighbors[c[0]] = neighbors.get(c[0], []) + [c[1]]
            neighbors[c[1]] = neighbors.get(c[1], []) + [c[0]]
            if c[0] in dic:
                dic[c[0]].add(c[1])
            else:
                dic[c[0]] = set([c[1]])

        queue = []
        for n in neighbors[0]:
            queue.append([0, n])
        while queue:
            curr = queue.pop(0)
            visited.add(curr[1])
            if curr[1] not in dic or curr[1] in dic and curr[0] not in dic[curr[1]]:
                res += 1
            for n in neighbors[curr[1]]:
                if n not in visited:
                    queue.append([curr[1], n])

        return res

test = Solution()
print test.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]])
print test.minReorder(5, [[1,0],[1,2],[3,2],[3,4]])
print test.minReorder(3, [[1,0],[2,0]])
print test.minReorder(4, [[0,1],[2,0],[3,2]])