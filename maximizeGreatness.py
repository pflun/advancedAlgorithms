# [1, 1, 1, 2, 3, 3, 5]   cnt is i, res is j
# ..i,j
#
# [1, 1, 1, 2, 3, 3, 5] => ans = 1;
# . i ...........j
#
# [1, 1, 1, 2, 3, 3, 5] => ans = 2;
# ..... i. ..........j
#
# [1, 1, 1, 2, 3, 3, 5] => ans = 3;
# ......... i . . . . . . j
#
# [1, 1, 1, 2, 3, 3, 5] => ans = 4;
# . . . . . . . .i . . . . . j
class Solution(object):
    def maximizeGreatness(self, nums):
        nums.sort()
        cnt = 0
        res = 0
        for num in nums:
            if num > nums[cnt]:
                res += 1
                cnt += 1
        return res