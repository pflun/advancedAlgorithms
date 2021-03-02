# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/discuss/1064548/JavaC%2B%2BPython-Binary-Search
# For example, the mid = 3,
# A[i] = 2, we split it into [2], and operations = 0
# A[i] = 3, we split it into [3], and operations = 0
# A[i] = 4, we split it into [3,1], and operations = 1
# A[i] = 5, we split it into [3,2], and operations = 1
# A[i] = 6, we split it into [3,3], and operations = 1
# A[i] = 7, we split it into [3,3,1], and operations = 2
# The number of operation we need is (a - 1) / mid
class Solution(object):
    def minimumSize(self, nums, maxOperations):
        lo = 1
        hi = 10 ** 9
        while lo <= hi:
            mid = (lo + hi) / 2
            if self.helper(nums, mid, maxOperations):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def helper(self, nums, min, maxOperations):
        cnt = 0
        for i in range(len(nums)):
            if nums[i] <= min:
                continue
            num = nums[i]
            if num % min == 0:
                cnt += num / min - 1
            else:
                cnt += num / min
        return True if cnt <= maxOperations else False

test = Solution()
print test.minimumSize([9], 2)
print test.minimumSize([2,4,8,2], 4)
print test.minimumSize([7,17], 2)