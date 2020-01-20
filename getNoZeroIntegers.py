class Solution(object):
    def getNoZeroIntegers(self, n):
        a = 1
        while a < n:
            if self.isValid(a) and self.isValid(n - a):
                return [a, n - a]
            a += 1
        return False

    def isValid(self, a):
        for c in str(a):
            if c == '0':
                return False
        return True

test = Solution()
print test.getNoZeroIntegers(2)
print test.getNoZeroIntegers(11)
print test.getNoZeroIntegers(10000)
print test.getNoZeroIntegers(69)
print test.getNoZeroIntegers(1010)