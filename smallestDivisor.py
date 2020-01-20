class Solution(object):
    def smallestDivisor(self, nums, threshold):
        if len(nums) == 1:
            d = 1
            while self.getDiv(nums, d) > threshold:
                d += 1
            return d
        high = max(nums)
        low = 1

        while low < high:
            mid = (low + high) / 2
            if self.getDiv(nums, mid) > threshold:
                low = mid + 1
            else:
                high = mid
        return low

    def getDiv(self, nums, mid):
        res = 0
        for n in nums:
            tmp = n / mid
            if n % mid != 0:
                tmp += 1
            res += tmp

test = Solution()
print test.smallestDivisor([1,2,5,9], 6)
print test.smallestDivisor([2,3,5,7,11], 11)
print test.smallestDivisor([19], 5)