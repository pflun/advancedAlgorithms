class Solution(object):
    def leftRigthDifference(self, nums):
        left = [0]
        right = [0]
        for n in nums[:-1]:
            left.append(left[-1] + n)
        for n in nums[len(nums):0:-1]:
            right = [n + right[0]] + right
        res = []
        for i in range(len(left)):
            res.append(abs(left[i] - right[i]))
        return res

test = Solution()
print test.leftRigthDifference([10,4,8,3])