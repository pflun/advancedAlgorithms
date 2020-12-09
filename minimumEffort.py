class Solution(object):
    def minimumEffort(self, tasks):
        tasks = sorted(tasks, key=lambda x: x[1] - x[0], reverse=True)
        totalCost = [x[0] for x in tasks]
        totalCost = sum(totalCost)
        maxRequired = [x[1] for x in tasks]
        maxRequired = max(maxRequired)
        res = max(totalCost, maxRequired)
        extra = res
        for t in tasks:
            need = t[1]
            actual = t[0]
            if res < need:
                extra += need - res
                res = need
            res -= actual
        return extra

test = Solution()
print test.minimumEffort([[1,2],[2,4],[4,8]])
print test.minimumEffort([[1,3],[2,4],[10,11],[10,12],[8,9]])
print test.minimumEffort([[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]])