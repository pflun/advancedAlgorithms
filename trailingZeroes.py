# trick: find how many 5 and 2, bc number of 0 rely on 5 * 2.
# b/c 2 is much more than 5, so we'll only need to find how many 5s
class Solution(object):
    def trailingZeroes(self, n):
        fives = 0
        for i in range(1, n + 1):
            while i % 5 == 0:
                fives += 1
                i /= 5
        return fives


    def trailingZeroesBrutalForce(self, n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        cnt = 0
        for i in range(len(str(res)) - 1, -1, -1):
            if str(res)[i] == '0':
                cnt += 1
            else:
                break

        return cnt

test = Solution()
print test.trailingZeroes(100)