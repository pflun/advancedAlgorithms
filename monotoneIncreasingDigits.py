# Optimization: https://leetcode.com/problems/monotone-increasing-digits/discuss/109794/Simple-Python-solution-w-Explanation

class Solution(object):
    def monotoneIncreasingDigits(self, N):
        if N < 10:
            return N

        def isIncreasing(num):
            num = str(num)
            for i in range(len(num) - 1):
                if num[i] > num[i + 1]:
                    return False

            return True

        while N > 0:
            if isIncreasing(N):
                return N
            else:
                N -= 1

test = Solution()
print test.monotoneIncreasingDigits(322)