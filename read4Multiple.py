class Solution(object):
    def __init__(self):
        self.p = 0
        self.buf = ''

    def read(self, buf, n):
        if n <= len(self.buf):
            tmp = self.buf[:len(n)]
            self.buf = self.buf[len(n):]
            return tmp
        else:
            res = self.buf
            self.buf = ''
            n -= len(res)
            for _ in range(n / 4):
                res += self.read4(buf)
            last = self.read4(buf)
            for _ in range(n % 4):
                if len(last) > 0:
                    tmp = last[0]
                    res += tmp
                    last = last[1:]
            self.buf = last
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
print test.read('123456789', 3)
print test.read('123456789', 4)
print test.read('123456789', 5)