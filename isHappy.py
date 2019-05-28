class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        tmp = 0
        sum = 0
        mem = set()
        while n >= 0:
            tmp = n % 10
            sum += tmp * tmp
            n /= 10
            if n == 0:
                if sum == 1:
                    return True
                if sum not in mem:
                    mem.add(sum)
                else:
                    return False
                n = sum
                sum = 0

    def isHappy2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n not in mem:
                mem.add(n)
            else:
                return False
        return True

test = Solution()
print test.isHappy(29)