# Reverse input (from right to left) then compare to original input
class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def palindrome(self, n):
        r = 0
        s = n
        if n == 0:
            return True
        elif n < 0:
            return False
        while n > 0:
            r *= 10
            r += n % 10
            n /= 10
        if s == r:
            return True
        else:
            return False

    def palindrome2(self, n):
        r = 0
        s = n
        if n == 0:
            return True
        elif n < 0:
            return False
        while n > 0:
            n, remainder = divmod(n, 10)
            r = r*10 + remainder
        if s == r:
            return True
        else:
            return False


test = Solution()
print test.palindrome2(121)