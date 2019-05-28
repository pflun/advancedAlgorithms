# Similar to Merge Intervals
class Solution(object):
    def meetingRooms(self, nums):
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i + 1][0] < sorted_nums[i][1]:
                return False
        return True

test = Solution()
print test.meetingRooms([[0, 5],[5, 10],[15, 20], [10, 15]])