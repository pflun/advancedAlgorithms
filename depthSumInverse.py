class Solution(object):
    def depthSumInverse(self, nestedList):
        self.res = 0
        # relative depth => val
        self.dic = {}
        # max depth for final calculation
        self.maxDepth = 0

        def dfs(A, depth):
            self.maxDepth = max(self.maxDepth, depth)
            if type(A) == int:
                if depth in self.dic:
                    self.dic[depth].append(A)
                else:
                    self.dic[depth] = [A]
            else:
                for a in A:
                    dfs(a, depth + 1)

        dfs(nestedList, 0)

        for k, v in self.dic.items():
            self.res += (self.maxDepth - k + 1) * sum(v)

        return self.res

test = Solution()
print test.depthSumInverse([1,[4,[6]]])