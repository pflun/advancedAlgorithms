class Solution(object):
    def subtractProductAndSum(self, n):
        nums = []
        while n != 0:
            nums.append(n % 10)
            n /= 10
        p = 1
        for num in nums:
            p *= num
        return p - sum(nums)

test = Solution()
print test.subtractProductAndSum(234)
print test.subtractProductAndSum(4421)