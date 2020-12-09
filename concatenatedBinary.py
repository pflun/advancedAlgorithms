import math
class Solution(object):
    def concatenatedBinary(self, n):
        res = 0
        length = 0
        for i in range(n, 0, -1):
            multiplier = math.pow(2, length)
            res += i * multiplier
            curr = bin(i)
            length += len(curr[2:])
        return int(res) % (10 ** 9 + 7)

test = Solution()
print test.concatenatedBinary(1)
print test.concatenatedBinary(3)
print test.concatenatedBinary(12)
print test.concatenatedBinary(42) # 727837408