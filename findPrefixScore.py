class Solution(object):
    def findPrefixScore(self, nums):
        max_arr = [nums[0]]
        for num in nums[1:]:
            max_arr.append(max(num, max_arr[-1]))
        conver = [2 * nums[0]]
        for i in range(1, len(nums)):
            conver.append(nums[i] + max_arr[i])
        res = [conver[0]]
        for conv in conver[1:]:
            res.append(conv + res[-1])
        return res