# -*- coding: utf-8 -*-
class Solution(object):
    # 类似单调栈，其实contest时写出来了
    # https://leetcode.com/problems/jump-game-vi/discuss/978497/Python-DP-%2B-Sliding-Window-Maximum-problem-combined
    """
        nums = [10,-5,-2,4,0,3], k = 3
        dp   = [10,5,8,14,14,17]

		this is what the deque looks likeat the beginning of each loop iteration
        deque = [(10,0)]        idx1
			    [(10,0),(5,1)]  idx2
				[(10,0),(8,2)]  idx3  #here the 8 was larger than 5 so it popped off the 5
				[(14,3)]        idx4  #here the 14 was larger than 8 and 10 so both of those were popped off
				[(14,3),(14,4)] idx5
	"""
    def maxResult2(self, nums, k):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        d = deque([(nums[0], 0)])
        for i in range(1, len(nums)):
            dp[i] = nums[i] + d[0][0]

            while d and d[-1][0] < dp[i]:
                d.pop()
            d.append((dp[i], i))

            if i - k == d[0][1]:
                d.popleft()

        return dp[-1]

    # TLE, k is 10 ^ 5
    def maxResult(self, nums, k):
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            curr = float('-inf')
            for j in range(max(0, i - k), i):
                curr = max(curr, dp[j] + nums[i])
            dp[i] = curr
        return dp[-1]

test = Solution()
print test.maxResult2([1,-1,-2,4,-7,3], 2)
print test.maxResult2([10,-5,-2,4,0,3], 3)
print test.maxResult2([1,-5,-20,4,-1,3,-6,-3], 2)