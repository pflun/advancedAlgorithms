class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        self.diff = float('inf')
        self.res = []
        for b in baseCosts:
            self.dfs(toppingCosts, target, b, 0)
        return min(self.res)

    def dfs(self, toppingCosts, target, price, idx):
        if idx > len(toppingCosts):
            return
        if price - target > self.diff:
            return
        if abs(price - target) < self.diff:
            self.diff = abs(price - target)
            self.res = [price]
        elif abs(price - target) == self.diff:
            self.res.append(price)
        for i in range(idx, len(toppingCosts)):
            self.dfs(toppingCosts, target, price, i + 1)
            self.dfs(toppingCosts, target, price + toppingCosts[idx], i + 1)
            self.dfs(toppingCosts, target, price + toppingCosts[idx] * 2, i + 1)

test = Solution()
print test.closestCost([1,7], [3,4], 10)
print test.closestCost([2,3], [4,5,100], 18)
print test.closestCost([3,10], [2,5], 9)
print test.closestCost([10], [1], 1)