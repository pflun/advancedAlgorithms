class Solution(object):
    def maxNiceDivisors(self, primeFactors):
        if primeFactors == 1:
            return 1
        if primeFactors == 2:
            return 2
        if primeFactors == 3:
            return 3

        if primeFactors % 3 == 0:
            rnt = pow(3, int(primeFactors / 3), (10 ** 9 + 7))
            return rnt % (10 ** 9 + 7)
        elif primeFactors % 3 == 1:
            rnt = 2 * 2 * pow(3, int(primeFactors / 3) - 1, (10 ** 9 + 7))
            return rnt % (10 ** 9 + 7)
        elif primeFactors % 3 == 2:
            rnt = 2 * pow(3, int(primeFactors / 3), (10 ** 9 + 7))
            return rnt % (10 ** 9 + 7)
        return 0

test = Solution()
print test.maxNiceDivisors(5)
print test.maxNiceDivisors(8)
print test.maxNiceDivisors(545918790)