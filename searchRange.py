class Solution(object):
    def searchRange(self, nums, target):
        res = []
        start = 0
        end = len(nums) - 1

        # binary search find first target from left
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] == target:
                res.append(mid)
                break
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        # target not found
        if len(res) == 0:
            return [-1, -1]

        # binary search find first larger than target
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid

        # first larger index - 1 is the last target index
        if low - 1 == res[0]:
            return res
        # append last target index
        elif low - 1 > res[0]:
            return res + [low - 1]

test = Solution()
print test.searchRange([5,7,7,8,8,10], 8)
print test.searchRange([5,7,7,8,8,10], 6)