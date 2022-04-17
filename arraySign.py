class Solution(object):
    def arraySign(self, nums):
        cnt = 0
        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                cnt += 1
        return 1 if cnt % 2 == 0 else -1

test = Solution()
print test.arraySign([-1,-2,-3,-4,3,2,1])
print test.arraySign([1,5,0,2,-3])
print test.arraySign([-1,1,-1,1,-1])