class Solution(object):
    def countPrimeSetBits(self, L, R):
        count = 0

        for n in range(L, R):
            bi = bin(n)[2:]
            ct = 0
            for b in bi:
                if b == 1:
                    ct += 1
            if self.isPrime(ct):
                count += 1

        return count

    def isPrime(self, num):
        for i in range(2, num):
            if num / i == 0:
                return False

        return True

test = Solution()
print test.countPrimeSetBits(6, 10)