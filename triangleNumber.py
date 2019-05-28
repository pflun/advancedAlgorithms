# https://www.youtube.com/watch?v=bojX9bdra-w
# kinda like 3 sum but only i += 1
class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        res = []
        # assume i <= j <= k
        for k in range(len(nums) - 1, 1, -1):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    for l in range(i, j):
                        res.append([nums[l], nums[j], nums[k]])
                    j -= 1
                else:
                    i += 1

        return res

test = Solution()
print test.triangleNumber([2,2,3,4])