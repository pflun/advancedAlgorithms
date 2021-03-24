class Solution(object):
    def reverse(self, x):
        if x > 0:
            sign = 1
        elif x < 0:
            x = -x
            sign = -1
        else:
            return 0
        res = []
        offset = 10
        while x > 0:
            res.append(x % offset)
            x = x / offset
        rnt = ''
        idx = 0
        for r in res:
            if r == 0:
                idx += 1
            else:
                break
        for i in range(idx, len(res)):
            rnt += str(res[i])
        return int(rnt) * sign

test = Solution()
print test.reverse(123)
print test.reverse(-123)
print test.reverse(120)
print test.reverse(0)