# https://leetcode.com/problems/read-n-characters-given-read4/
class Solution:
    def read(self, buf, n):
        res = ''
        if n % 4 == 0:
            for _ in range(n / 4):
                res += self.read4(buf)
        else:
            for _ in range(n / 4 + 1):
                res += self.read4(buf)
            res = res[:len(res) - (4 - n % 4)]

        return res

    def read4(self, buf):
        # iterate read 4 char a time, if 3 char left then return 3 char
        return
