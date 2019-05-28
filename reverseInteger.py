class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        r = 0
        if n == 0:
            return 0
        elif n < 0:
            n = -n
            while n > 0:
                r *= 10
                r += n % 10
                n /= 10
            return -r
        while n > 0:
            r *= 10
            r += n % 10
            n /= 10

        return r

class SolutionUp:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        r = 0
        if n == 0:
            return 0
        while n < 0:
            r *= 10
            r -= n % 10
            n /= 10
        while n > 0:
            r *= 10
            r += n % 10
            n /= 10
            return r


test = SolutionUp()
print test.reverseInteger(-188)