# Implement rand25() using rand5() function.
import random
class Solution(object):
    def rand25(self):
        bucket = random.randint(0, 4)
        # e.g. 0 * 5 + 3 = 3; 4 * 5 + 3 = 23
        return bucket * 5 + self.rand5()

    # Reservoir Sampling, or just use randint(1, 5)
    def rand5(self):
        nums = [1, 2, 3, 4, 5]
        for i in range(len(nums)):
            index = random.randint(0, i)
            nums[index], nums[i] = nums[i], nums[index]
        return nums[0]

test = Solution()
print test.rand25()