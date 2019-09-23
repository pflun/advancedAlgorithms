class Solution(object):
    def minimumAbsDifference(self, arr):
        arr = sorted(arr)
        mini = float('inf')
        res = []
        for i in xrange(1, len(arr)):
            a = arr[i - 1]
            b = arr[i]
            if b - a == mini:
                res.append([a, b])
            elif b - a < mini:
                res = [[a, b]]
                mini = b - a
        return res

test = Solution()
print test.minimumAbsDifference([3,8,-10,23,19,-4,-14,27])
print test.minimumAbsDifference([4,2])