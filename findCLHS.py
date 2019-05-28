# Find Consecutive Longest Harmonious Subsequence

class Solution(object):
    def findCLHS(self, nums):
        res = 1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                tmp = set(nums[i:j + 1])
                if len(tmp) == 2 and abs(list(tmp)[0] - list(tmp)[1]) == 1:
                    res = max(res, j - i + 1)

        return res


test = Solution()
print test.findCLHS([1,3,2,2,5,2,3,7])