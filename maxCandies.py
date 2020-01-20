class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        self.visited = set()
        self.res = 0
        for b in initialBoxes:
            self.dfs(status, candies, keys, containedBoxes, b, set(), set())
        return self.res

    def dfs(self, status, candies, keys, containedBoxes, currBox, hasKeys, hasBoxes):
        if currBox in self.visited:
            return
        if status[currBox] == 1 or currBox in hasKeys:
            self.visited.add(currBox)
            self.res += candies[currBox]
            for b in containedBoxes[currBox]:
                hasBoxes.add(b)
                self.dfs(status, candies, keys, containedBoxes, b, hasKeys, hasBoxes)
            if len(keys[currBox]) != 0:
                for k in keys[currBox]:
                    if k in hasBoxes:
                        hasKeys.add(k)
                        self.dfs(status, candies, keys, containedBoxes, k, hasKeys, hasBoxes)

test = Solution()
print test.maxCandies([1,0,1,0],[7,5,4,100],[[],[],[1],[]],[[1,2],[3],[],[]],[0])
print test.maxCandies([1,0,0,0,0,0],[1,1,1,1,1,1],[[1,2,3,4,5],[],[],[],[],[]],[[1,2,3,4,5],[],[],[],[],[]],[0])
print test.maxCandies([1,1,1],[100,1,100],[[],[0,2],[]],[[],[],[]],[1])
print test.maxCandies([1],[100],[[]],[[]],[])
print test.maxCandies([1,1,1],[2,3,2],[[],[],[]],[[],[],[]],[2,1,0])
