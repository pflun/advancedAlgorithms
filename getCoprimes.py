class Solution(object):
    # Brutal force
    def getCoprimes(self, nums, edges):
        self.res = [-1]
        self.graph = {}
        for e in edges:
            self.graph[max(e[0], e[1])] = min(e[0], e[1])
        for i in range(1, len(nums)):
            self.dfs(nums, i, self.graph[i])
        return self.res

    def dfs(self, nums, start, curr):
        if curr == 0:
            if self.isCoprime(nums, start, curr):
                self.res.append(0)
                return
            else:
                self.res.append(-1)
                return
        if self.isCoprime(nums, start, curr):
            self.res.append(curr)
        else:
            self.dfs(nums, start, self.graph[curr])

    def isCoprime(self, nums, start, curr):
        if self.gcd(nums[start], nums[curr]) == 1:
            return True
        else:
            return False

    # greatest common divisor
    def gcd(self, x, y):
        if x % y == 0:
            return y
        else:
            return self.gcd(y, x % y)

test = Solution()
print test.getCoprimes([2,3,3,2], [[0,1],[1,2],[1,3]])
print test.getCoprimes([5,6,10,2,3,6,15], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]])