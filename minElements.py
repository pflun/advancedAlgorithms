class Solution(object):
    def minElements(self, nums, limit, goal):
        sumVal = sum(nums)
        diff = goal - sumVal
        if diff % limit == 0:
            return abs(diff)/ limit
        else:
            return abs(diff) / limit + 1

test = Solution()
print test.minElements([1,-1,1], 3, -4)
print test.minElements([1,-10,9,1], 100, 0)