class Solution:
    # @param {integer[]} nums
    # @return {string}
    # bubble sort
    def largestNumber(self, nums):
        for i in xrange(len(nums), 0, -1):
            for j in xrange(i - 1):
                if not self.compare(nums[j], nums[j + 1]):
                    # exchange
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return ''.join(str(x) for x in nums)
        # return str(int("".join(map(str, nums))))

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

test = Solution()
print test.largestNumber([2, 18, 9, 22, 17, 24, 8, 12, 27])
print test.compare(12, 27)