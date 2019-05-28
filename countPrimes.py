# Sieve of Eratosthenes

class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        counter = 0
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2, n):
            if res[i] == True:
                for j in range(i + 1, n):
                    if j % i == 0:
                        res[j] = False

        for x in range(len(res)):
            if res[x] == True:
                counter += 1

        return counter

test = Solution()
print test.countPrimes(20)