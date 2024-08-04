# A special number must be a square of a prime number.
import math
class Solution(object):
    def nonSpecialCount(self, l, r):
        lim = int(math.sqrt(r))
        # Create a list to mark primes up to lim using Sieve of Eratosthenes
        is_prime = [True] * (lim + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

        # Sieve of Eratosthenes to mark non-prime numbers
        for i in range(2, int(math.sqrt(lim)) + 1):
            if is_prime[i]:
                for j in range(i * i, lim + 1, i):
                    is_prime[j] = False

        # Count special numbers in the range [l, r]
        special_count = 0
        for i in range(2, lim + 1):
            if is_prime[i]:
                square = i * i
                if l <= square <= r:
                    special_count += 1

        # Total numbers in the range [l, r]
        total_count = r - l + 1

        # Calculate non-special numbers
        return total_count - special_count

test = Solution()
print test.nonSpecialCount(5, 7)
print test.nonSpecialCount(4, 16)
print test.nonSpecialCount(1, 99)
