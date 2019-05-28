class Solution(object):
    def checkPossibility(self, nums):
        if len(nums) <= 2:
            return True

        count = 0
        target = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                target = i

        if count > 1:
            return False
        else:
            if target == 0:
                return True
            elif target == len(nums) - 2:
                return True
            else:
                # Change target next
                if nums[target + 2] - nums[target] > 0:
                    return True
                # Change target
                elif nums[target + 1] - nums[target - 1] > 0:
                    return True
                else:
                    return False



test = Solution()
print test.checkPossibility([2,3,3,2,4])