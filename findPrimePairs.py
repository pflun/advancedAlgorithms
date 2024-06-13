class Solution(object):
    def findPrimePairs(self, n):
        if n == 1 or n == 2:
            return []
        res = []
        prime = self.countPrimes(n)
        for i in range(2, n / 2 + 1):
            if prime[i] and prime[n - i]:
                res.append([i, n - i])
        return res

    # find all prime numbers using Sieve of Eratosthenes algorithm
    def countPrimes(self, n):
        prime = [True] * (n + 1)
        prime[1] = False
        prime[0] = False
        p = 2
        while p ** 2 <= n:
            if prime[p]:
                for i in range(p ** 2, n + 1, p):
                    prime[i] = False
            p += 1

        return prime

    # TLE if check prime number one by one
    def isPrime(self, n):
        divisor = 2
        while n > divisor:
            if n % divisor == 0:
                return False
            else:
                divisor += 1
        return True

test = Solution()
print test.findPrimePairs(10)
print test.findPrimePairs(2)
print test.countPrimes(10)