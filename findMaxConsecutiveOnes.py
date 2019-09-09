class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        res = 0
        for n in nums:
            if n == 1:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 0
        return res

test = Solution()
print test.findMaxConsecutiveOnes([1,1,0,1,1,1])