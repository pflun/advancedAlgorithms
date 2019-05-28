class Solution:
    """
    @param a: The first integer
    @param b: The second integer
    @return:  The sum of a and b
    """
    def aplusb(self, a, b):
        # eventually b will be 0 after continuely >> 1
        if b == 0:
            return a
        # elif (a > 0 and b < 0) or (a < 0 and b > 0):
        #     c = a ^ b
        #     d = (a & b) >> 1
        #     return self.aplusb(c, d)
        else:
            c = a ^ b
            d = (a & b) << 1
            return self.aplusb(c, d)

test = Solution()
print test.aplusb(1, 100)

c = 3 ^ 5
d = (3 & 5) << 1

print c, d