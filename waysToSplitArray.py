class Solution(object):
    def waysToSplitArray(self, nums):
        res = 0
        prefix = []
        for n in nums:
            if len(prefix) == 0:
                prefix.append(n)
            else:
                prefix.append(n + prefix[-1])
        for i in range(len(nums) - 1):
            if prefix[i] >= prefix[-1] - prefix[i]:
                res += 1
        return res

test = Solution()
print test.waysToSplitArray([10,4,-8,7])
print test.waysToSplitArray([2,3,1,0])