# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/discuss/477666/Python-solution-easy-to-understand
class Solution(object):
    def minFlips(self, a, b, c):
        res = 0
        while (a | b) != c:
            ai = a % 2
            bi = b % 2
            ci = c % 2

            if ai | bi != ci:
                res += ai + bi + ci

            a /= 2
            b /= 2
            c /= 2

        return res

test = Solution()
print test.minFlips(2, 6, 5)
print test.minFlips(4, 2, 7)
print test.minFlips(1, 2, 3)