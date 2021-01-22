class Solution(object):
    def maximumUniqueSubarray(self, nums):
        left = 0
        right = 1
        curr = nums[0]
        res = curr
        hashSet = set([nums[0]])
        while right < len(nums):
            if nums[right] not in hashSet:
                hashSet.add(nums[right])
                curr += nums[right]
                right += 1
                res = max(res, curr)
            else:
                hashSet.remove(nums[left])
                curr -= nums[left]
                left += 1
        return res

test = Solution()
print test.maximumUniqueSubarray([4,2,4,5,6])
print test.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5])