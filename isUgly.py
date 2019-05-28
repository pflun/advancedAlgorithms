class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        if num <= 0:
            return False
        for x in [2, 3, 5]:
            while num % x == 0:
                num = num / x
                # print num
        return num == 1

test = Solution()
print test.isUgly(90)