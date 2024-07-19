class Solution(object):
    # https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/solutions/5352862/greedy/
    def minOperations(self, nums):
        res = 0
        # To avoid TLE, memorize flipped/not flipped state after each 0->1
        flipped = False
        for i in range(len(nums)):
            if nums[i] == 0 and flipped == False:
                res += 1
                flipped = not flipped
            elif nums[i] == 1 and flipped == True:
                res += 1
                flipped = not flipped
        return res

test = Solution()
print test.minOperations([0,1,1,0,1])
print test.minOperations([1,0,0,0])