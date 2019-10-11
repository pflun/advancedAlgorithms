class Solution(object):
    def __init__(self):
        self.p = 0

    def read(self, buf, n):
        res = ''
        for _ in range(n / 4):
            res += self.read4(buf)
        last = self.read4(buf)
        for _ in range(n % 4):
            if len(last) > 0:
                tmp = last[0]
                res += tmp
                last = last[1:]
        return res

    def read4(self, buf):
        if len(buf[self.p:]) >= 4:
            res = buf[self.p:self.p + 4]
            self.p += 4
        else:
            res = buf[self.p:]
            self.p = len(buf)
        return res

test = Solution()
print test.read4('123456789')
print test.read('123456789', 6)