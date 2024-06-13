class Solution(object):
    def maxScore(self, nums):
        rearrange = sorted(nums, reverse=True)
        prefix = [rearrange[0]]
        for a in rearrange[1:]:
            prefix.append(prefix[-1] + a)
        res = 0
        for a in prefix:
            if a > 0:
                res += 1
            else:
                break
        return res

test = Solution()
print test.maxScore([2,-1,0,1,-3,3,-3])