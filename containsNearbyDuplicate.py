class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) == 0:
            return False

        if k <= 1:
            return False

        for i in range(k - 1, len(nums) - k):
            tmp = set(nums[i:i + k])
            print tmp
            if len(tmp) < k:
                return True
        return False

test = Solution()
print test.containsNearbyDuplicate([-2,1,-3,4,-1,2,1,-5, -5,4], 3)