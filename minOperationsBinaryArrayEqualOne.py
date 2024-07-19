class Solution(object):
    def minOperations2(self, nums):
        res = 0
        for i in range(len(nums) - 3):
            if nums[i] == 0:
                res += 1
                nums[i + 1] = self.flip(nums[i + 1])
                nums[i + 2] = self.flip(nums[i + 2])
            else:
                continue
        if not all(v == nums[-3:][0] for v in nums[-3:]):
            return -1
        elif all(v == 0 for v in nums[-3:]):
            return 1 + res
        elif all(v == 1 for v in nums[-3:]):
            return res

    # memory exceed, should've use iteration
    def minOperations(self, nums):
        if len(nums) == 3 and not all(v == nums[0] for v in nums): # nums[0] == nums[1] == nums[2]:
            return -1
        elif len(nums) == 3 and all(v == 0 for v in nums):
            return 1
        elif len(nums) == 3 and all(v == 1 for v in nums):
            return 0
        if nums[0] == 0:
            rest = self.minOperations([self.flip(nums[1])] + [self.flip(nums[2])] + nums[3:])
            return rest if rest == -1 else 1 + rest
        else:
            rest = self.minOperations(nums[1:])
            return rest

    def flip(self, num):
        return 1 - num

test = Solution()
print test.minOperations2([0,1,1,1,0,0])
print test.minOperations2([0,1,1,1])
print test.minOperations2([1,0,0,1,1,1,0,1,1,1])
print test.minOperations2([1,0,0,0])