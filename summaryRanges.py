class Solution(object):
    def summaryRanges(self, nums):

        range_results = []
        tmp_start = None
        tmp_end = None

        for i in range(1, len(nums)):
            # Set up lower range
            if tmp_start == None:
                tmp_start = nums[i - 1]
            # Check last element
            if nums[i] - nums[i - 1] > 1 and i == len(nums) - 1:
                range_results.append(nums[i])
            # Check first element
            elif nums[i] - nums[i - 1] > 1 and i == 1:
                range_results.append(nums[i - 1])
            # Check middle single element, note border
            elif nums[i] - nums[i - 1] > 1 and nums[i + 1] - nums[i ] > 1 and i != len(nums) - 1:
                range_results.append(nums[i])
            # Check middle range
            if nums[i] - nums[i - 1] == 1:
                continue
            else:
                tmp_end = nums[i - 1]
                range_result = str(tmp_start) + "->" + str(tmp_end)
                range_results.append(range_result)
                tmp_start = None
                tmp_end = None
        return range_results

test = Solution()
print test.summaryRanges([0,1,2,4,5,7])
