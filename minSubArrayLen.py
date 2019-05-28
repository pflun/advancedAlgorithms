# Two pointer chasing

class Solution(object):
    def minSubArrayLen(self, s, nums):
        j = 0
        res = float("inf")
        sum = 0

        for i in range(len(nums)):
            while j < len(nums) and sum < s:
                sum += nums[j]
                j += 1
            if sum >= s:
                res = min(res, j - i)
            sum -= nums[i]

        if res == float("inf"):
            res = 0
        return res

    def minSubArrayLen2(self, s, nums):
        slow = 0
        fast = 0
        res = float("inf")
        while fast < len(nums):
            tmp = 0
            for i in range(slow, fast + 1):
                tmp += nums[i]
            if tmp >= s:
                res = min(res, fast - slow + 1)
                slow += 1
            else:
                fast += 1
        if res == float("inf"):
            res = 0
        return res

test = Solution()
print test.minSubArrayLen2(7, [2,3,1,2,4,3])