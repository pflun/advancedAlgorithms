class Solution(object):
    def numSteps(self, s):
        if s == "1":
            return 0
        n = int(s, 2)
        step = 0
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                n += 1
            step += 1
        return step

test = Solution()
print test.numSteps("1101")
print test.numSteps("10")
print test.numSteps("1")