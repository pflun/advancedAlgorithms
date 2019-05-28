class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, nums):
        p = 0
        ans = 0
        for item in nums[:-1]:
            # max(previous can jump position, curr position + curr can jump)
            ans = max(ans, p + item)
            # not able to jump to next position
            if ans <= p:
                return False
            # position proceed one step (one more level)
            p += 1
        return True

test = Solution()
print test.canJump([3,2,1,0,4])