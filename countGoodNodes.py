class Solution(object):
    # Bug, it's undirected tree and root is not necessarily 0, you'll have to find the root first
    def countGoodNodes(self, edges):
        self.res = 0
        self.graph = {}
        for e in edges:
            self.graph[e[0]] = self.graph.get(e[0], []) + [e[1]]

        # return children size
        def helper(curr):
            # leaf
            if curr not in self.graph:
                self.res += 1
                return 1
            children = self.graph[curr]
            # check if same size
            tmp = []
            for c in children:
                tmp.append(helper(c))
            # check if all elements are identical
            if all(i == tmp[0] for i in tmp):
                self.res += 1
            return sum(tmp)

        helper(0)
        return self.res

test = Solution()
# print test.countGoodNodes([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]])
# print test.countGoodNodes([[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]])
# print test.countGoodNodes([[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]])
print test.countGoodNodes([[6,0],[1,0],[5,1],[2,5],[3,1],[4,3]])