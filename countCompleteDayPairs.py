class Solution(object):
    def countCompleteDayPairs(self, hours):
        if len(hours) == 1:
            return 0

        res = 0
        remainder_count = {0: 0}
        for i in range(len(hours)):
            remainder = hours[i] % 24
            if remainder == 0:
                res += remainder_count[0]
            else:
                if 24 - remainder in remainder_count:
                    res += remainder_count[24 - remainder]
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        return res

test = Solution()
print test.countCompleteDayPairs([12,12,30,24,24])
print test.countCompleteDayPairs([72,48,24,3])