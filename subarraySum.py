# -*- coding: utf-8 -*-
# 跟2sum异曲同工, https://leetcode.com/problems/subarray-sum-equals-k/discuss/102106/Java-Solution-PreSum-%2B-HashMap
# preSum的n^2解法可过OJ，[i, j] = [0, j] - [0, i]
class Solution(object):
    def subarraySum3(self, nums, k):
        # Same as 2
        preSum = [nums[0]]
        for n in nums[1:]:
            preSum.append(n + preSum[-1])
        res = 0
        dic = {}
        for n in preSum:
            if n == k:
                res += 1
            if n - k in dic:
                res += dic[n - k]
            dic[n] = dic.get(n, 0) + 1
        return res

    def subarraySum2(self, nums, k):
        res = 0
        # sum => freq
        dic = {}
        preSum = 0
        # having initialize preSum.put(0,1)....it is for those (sum - k) == 0 calculations which are valid subarrays but need to get counted.
        # e.g. if k = 7 and sum = 7 (at second element for array is : 3, 4, 3, 8) at some iteration.....then sum - k = 0....this 0 will get counted in statement result += preSum.get(sum - k);
        # either initialize this: dic[0] = 1 or if preSum == k: res += 1
        for n in nums:
            preSum += n
            if preSum == k:
                res += 1
            # 在dic中找到一组结果，使得preSum - t = k，就加入res
            if preSum - k in dic:
                res += dic[preSum - k]
            dic[preSum] = dic.get(preSum, 0) + 1

        return res

    # sliding window m没有考虑负数情况
    def subarraySum(self, nums, k):
        if len(nums) == 0 or not k:
            return 0

        res = 0
        tmp = 0
        left = 0
        right = 0

        while right < len(nums):
            if tmp == k:
                res += 1
                tmp -= nums[left]
                left += 1
            elif tmp < k:
                tmp += nums[right]
                right += 1
            else:
                tmp -= nums[left]
                left += 1

        if tmp == k:
            res += 1

        return res

test = Solution()
print test.subarraySum2([1,1,-1,1], 1)