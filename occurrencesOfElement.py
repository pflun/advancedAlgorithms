class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        occurrences = []
        for i in range(len(nums)):
            if nums[i] == x:
                occurrences.append(i)
        res = []
        for q in queries:
            if q > len(occurrences):
                res.append(-1)
            else:
                res.append(occurrences[q - 1])
        return res

test = Solution()
print test.occurrencesOfElement([1,3,1,7], [1,3,2,4], 1)
print test.occurrencesOfElement([1,2,3], [10], 5)