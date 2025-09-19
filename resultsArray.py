# count consecutive elements as we go
# nums[i + 1] is the Power
class Solution(object):
    def resultsArray(self, nums, k):
        if k == 1:
            return nums
        res = []
        cnt = 1
        for i in range(len(nums) - 1):
            # count how many consecutive elements at i + 1
            if nums[i + 1] - nums[i] == 1:
                cnt += 1
            else:
                cnt = 1
            # sliding window start to append result, a size k window end at i + 1
            if i >= k - 2:
                # there're more consecutive elements than k needed
                if cnt >= k:
                    res.append(nums[i + 1])
                else:
                    res.append(-1)
        return res

test = Solution()
print test.resultsArray([1,2,3,4,3,2,5], 3)
print test.resultsArray([2,2,2,2,2], 4)
print test.resultsArray([3,2,3,2,3,2], 2)