# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/solutions/3312034/python-simulation/
# similar to for a,i in sorted([a,i] for i,a in enumerate(A)): already sort by value && contains original index
class Solution(object):
    def findScore(self, nums):
        sorted_nums = []
        for i in range(len(nums)):
            sorted_nums.append([nums[i], i])
        # [value, original_index]
        sorted_nums.sort()
        seen = [False for _ in range(len(nums))]
        res = 0
        for num, idx in sorted_nums:
            if seen[idx]:
                continue
            res += num
            seen[idx] = True
            if idx - 1 >= 0:
                seen[idx - 1] = True
            if idx + 1 <= len(nums) - 1:
                seen[idx + 1] = True
        return res