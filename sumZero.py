class Solution(object):
    def sumZero(self, n):
        if n == 1:
            return [0]
        if n % 2 == 0:
            res = []
        else:
            res = [0]
        tmp = 1
        for _ in range(n / 2):
            res.append(tmp)
            res.append(-tmp)
            tmp += 1
        return res

test = Solution()
print test.sumZero(5)
print test.sumZero(3)
print test.sumZero(4)